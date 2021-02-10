# -*- encoding:utf-8 -*-
# 开发团队：大数据组
# 开发者：albert·bing
# 开发时间：2020/7/5 20:13
# 文件名称：yellow_calendar.py
# 开发工具：PyCharm


#  start your code


import sys
sys.path.append('/home/hadoop/programs/spider/WTP66_BigdataCrawler')
# 导入selenium的驱动接口
from selenium import webdriver
# 导入键盘操作的keys包
from selenium.webdriver.common.action_chains import ActionChains
# 导入chrome选项
from selenium.webdriver.chrome.options import Options

from crawler.com.wt.config import config

import json

from crawler.com.wt.common import MysqlUtil

import requests
from bs4 import BeautifulSoup
import urllib3
import time

# 忽略https的安全警告
urllib3.disable_warnings()




number="297"


def initClassNumber(driver):
    driver.get("https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_3#tab0")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    tmp = str(soup.select('.mola-window')[0]).split(">")[1].split("-")[2].split("_")[0]
    return tmp

# 获取省份的当日数据--并且插入
def get_data_resource_province(driver):
    # https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_3#tab0
    driver.get("https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_3#tab0")
    # 屏幕向下滚动，获取点击事件
    # driver.execute_script("window.scrollTo(0,1000);")
    # 点击打开省份的下拉列表  Common_1-1-295_3lDRV2
    driver.find_element_by_class_name("Common_1-1-"+number+"_3lDRV2").click()
    # 屏幕向下滚动，获取点击事件
    driver.execute_script("window.scrollTo(0,1000);")
    driver.find_element_by_class_name("Common_1-1-"+number+"_3lDRV2").click()

    soup = BeautifulSoup(driver.page_source, "html.parser")
    pro_trs_data = soup.find_all("tr", attrs={"class": "VirusTable_1-1-"+number+"_3m6Ybq"})

    time_file = driver.find_element_by_class_name("Virus_1-1-"+number+"_32Y_aO")
    today_time = time_file.text.split(" ")[1]

    insert_pro_data = []
    # 循环获取所有的省份
    for num in range(0, len(pro_trs_data), 1):
        p_data = []
        tt = pro_trs_data[num].select("td")
        p_data.append(today_time)
        p_data.append(tt[0].text)
        p_data.append(tt[0].text)
        p_data.append(tt[1].text)
        p_data.append(tt[2].text)
        p_data.append(tt[3].text)
        p_data.append(tt[4].text)
        p_data.append(tt[5].text)
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        p_data.append(create_time)
        p_data.append(update_time)
        insert_pro_data.append(p_data)

    # 插入所有省的当日数据
    # print(insert_pro_data)
    MysqlUtil.insert_internal_cur_day_data(insert_pro_data)

    return insert_pro_data


# 获取城市的当日的数据---并且插入
def get_data_resource_city(driver, pro_list):
    driver.get("https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_3#tab0")
    # 因为上一个方法已经打开下拉菜单，所以这里就不在重复打开了
    # driver.find_element_by_class_name("Common_1-1-279_3lDRV2").click()

    trs_list = driver.find_elements_by_class_name("VirusTable_1-1-"+number+"_3m6Ybq")
    # 屏幕向下滚动，获取点击事件
    driver.execute_script("window.scrollTo(0,1000);")

    time_file = driver.find_element_by_class_name("Virus_1-1-"+number+"_32Y_aO")
    today_time = time_file.text.split(" ")[1]

    # 循环点击，将所有的都点开
    for num in range(0, len(trs_list)):
        trs_list[num].click()
        # 存放一个省的市的数据
        c_list = []
        soup = BeautifulSoup(driver.page_source, "html.parser")
        city_trs_data = soup.find_all("tr", attrs={"class": "VirusTable_1-1-"+number+"_2AH4U9"})
        tds = city_trs_data[0].select("td")
        if tds[0].text == '美国':
            continue
        # print(pro_list[num][0], tds[0].text)
        for n in range(0, len(city_trs_data), 1):
            p_data = []
            tt = city_trs_data[n].select("td")
            if tt[0].text == '美国':
                break
            else:
                p_data.append(today_time)
                p_data.append(pro_list[num][1])
                p_data.append(tt[0].text)
                p_data.append(tt[1].text)
                p_data.append(tt[2].text)
                p_data.append(tt[3].text)
                p_data.append(tt[4].text)
                p_data.append(tt[5].text)
                create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                p_data.append(create_time)
                p_data.append(update_time)
                c_list.append(p_data)

        # 一个省的市数据，批量插入一次
        # print(c_list)
        MysqlUtil.insert_internal_cur_day_data(c_list)

        city_trs_data = []
        tds = []
        # 点击关闭
        trs_list[num].click()

# 获取省份的外来输入人数的数据
def get_import_abroad_data(driver, pro_list):
    driver.get("https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_3#tab0")
    # 因为上一个方法已经打开下拉菜单，所以这里就不在重复打开了
    # driver.find_element_by_class_name("Common_1-1-279_3lDRV2").click()

    trs_list = driver.find_elements_by_class_name("VirusTable_1-1-" + number + "_3m6Ybq")
    # 屏幕向下滚动，获取点击事件
    driver.execute_script("window.scrollTo(0,1000);")
    # 获取时间
    time_file = driver.find_element_by_class_name("Virus_1-1-" + number + "_32Y_aO")
    today_time = time_file.text.split(" ")[1]

    import_list = []

    # 循环点击，将所有的都点开
    for num in range(0, len(trs_list)):
        trs_list[num].click()
        # 存放一个省的境外输入的数据
        # import_list = []
        soup = BeautifulSoup(driver.page_source, "html.parser")
        table_data = soup.find_all("table",attrs={"class":"VirusTable_1-1-"+number+"_3U6wJT"})
        city_trs_data = table_data[0].find_all("tr")
        tds = city_trs_data[0].select("td")
        if tds[0].text == '美国':
            continue
        # print(pro_list[num][0], tds[0].text)
        for n in range(0, len(city_trs_data), 1):
            p_data = []
            tt = city_trs_data[n].select("td")
            if tt[0].text != '境外输入':
                break
            else:
                p_data.append(today_time)
                p_data.append(pro_list[num][1])
                p_data.append(tt[0].text)
                p_data.append(tt[1].text)
                p_data.append(tt[2].text)
                p_data.append(tt[3].text)
                p_data.append(tt[4].text)
                p_data.append(tt[5].text)
                create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                p_data.append(create_time)
                p_data.append(update_time)
                # 先判断是否为空，如果为空则不执行数据追加
                if p_data:
                    import_list.append(p_data)
        city_trs_data = []
        tds = []
        # 点击关闭
        trs_list[num].click()
    # 一个省的市数据，批量插入一次
    # print(import_list)
    MysqlUtil.insert_import_abroad(import_list)

# 创建driver
def create_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=config._CHROME_DRIVER_LINUX, options=chrome_options)
    return driver


if __name__ == '__main__':
    driver = create_driver()

    # 初始化classnumber
    tmp = initClassNumber(driver=driver)
    number = tmp
    time.sleep(5)

    # 获取历史疫情数据
    # get_data_resource_province_history(driver)
    # 获取省份的当日疫情数据
    pro_list = get_data_resource_province(driver)
    # 获取城市的当日疫情数据
    get_data_resource_city(driver, pro_list)
    # 获取境外输入的省份
    get_import_abroad_data(driver,pro_list)
    time.sleep(5)
    # 给数据添加area_id
    MysqlUtil.insert_internal_cur_day_data_add_areaId()
    time.sleep(1)
