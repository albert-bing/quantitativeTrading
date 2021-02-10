# -*- encoding:utf-8 -*-
# 开发团队：大数据组
# 开发者：albert·bing
# 开发时间：2020/7/5 20:13
# 文件名称：yellow_calendar.py
# 开发工具：PyCharm


#  start your code

# import sys
# sys.path.append('/home/hadoop/programs/spider/WTP66_BigdataCrawler')

# 导入selenium的驱动接口
from selenium import webdriver
# 导入键盘操作的keys包
from selenium.webdriver.common.action_chains import ActionChains
# 导入chrome选项
from selenium.webdriver.chrome.options import Options

from com.code.lxb.config import config

import json

# from crawler.com.wt.common import MysqlUtil
# import requests
from bs4 import BeautifulSoup
import urllib3
import time

# 忽略https的安全警告
urllib3.disable_warnings()



#  description：主要是获取公司的股票代码



def getData(driver):
    driver.get("https://www.banban.cn/gupiao/list_sh.html")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    divs = soup.findAll("div",attrs={"class","u-postcontent cz"})
    alist = divs[0].find_all("a")
    code_list = []
    for i in range(0,len(alist),1):
        one_list = []
        tmp = alist[i].text.split("(")
        one_list.append(tmp[0])
        one_list.append(tmp[1].split(")")[0])
        code_list.append(one_list)
    print(code_list)


# 创建driver
def create_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=config._CHROME_DRIVER_WIN, options=chrome_options)
    return driver


if __name__ == '__main__':
    driver = create_driver()
    getData(driver)
