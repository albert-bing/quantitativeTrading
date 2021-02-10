# -*- encoding:utf-8 -*-
# 开发团队：大数据组
# 开发者：albert·bing
# 开发时间：2020/7/5 20:13
# 文件名称：yellow_calendar.py
# 开发工具：PyCharm


#  start your code

import logging
import pymongo
from pymongo import GEO2D

host = '172.21.0.2'
user = "admin"
passwd = "Autopai2018"
# 更新数据
def update_data_ford(result_data):
    logging.info("数据开始更新.....")
    myclient = pymongo.MongoClient(host=host, port=27017)
    db = myclient.admin
    db.authenticate(user, passwd)
    my_db = myclient.poi
    mycol = my_db.ford_website_sales
    for i in range(0, len(result_data), 1):
        mycol.insert_one(eval(result_data[i]))
    # mycol.create_index([("location", GEO2D)], name='location')
    logging.info("数据更新完成！！")


# 移除消失的经销商
def remove_fords_data(data):
    logging.info("数据开始移除.....")
    myclient = pymongo.MongoClient(host=host, port=27017)
    db = myclient.admin
    db.authenticate(user, passwd)
    my_db = myclient.poi
    mycol = my_db.ford_website_sales
    for i in range(0, len(data), 1):
        mycol.delete_one({'name': data[i]['name']})
    logging.info("数据移除完成！！")


# 查询所有已存好的数据
def select_fords_all():
    myclient = pymongo.MongoClient(host=host, port=27017)
    db = myclient.admin
    db.authenticate(user, passwd)
    my_db = myclient.poi
    mycol = my_db.ford_website_sales
    data_all = mycol.find()
    count = mycol.count()
    return data_all, count