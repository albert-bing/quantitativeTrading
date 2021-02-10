# @Team：Big Data Group
# @Time：2020/7/6 16:10
# @Author：albert·bing
# @File：MysqlUtil.py
# @Software：PyCharm


#  start your code

import pymysql

# 测试
host = '81.70.166.101'
# 生产
# host='172.21.0.49'
password = 'r1kJzB'
port = 3306

# 黄历数据入库
def insert_data_yellow_calendar(data):
    db = pymysql.connect(host=host, user='root', password=password, port=port, db='traffic')
    cursor = db.cursor()
    # sql = "select * from car_param_info limit 10;"
    sql = 'insert into date_yellow_calendar(`y_day`,`gregorian_calendar`,`lunar_calendar`,`dao`,`start`,`yi`,`ji`,`chong`,\
    `suici`,`tai`,`wuxing`,`cai`,`xi`,`fu`,`constellation`,`chinese_zodiac`,`xiongshen`,`jishen`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cursor.executemany(sql, data)
    cursor.close()
    db.commit()
    db.close()
    print("mysql-插入成功！\n")

# 查询日期
def select_data_date(start_date,end_date):
    db = pymysql.connect(host=host, user='root', password=password, port=port, db='traffic')
    cursor = db.cursor()
    # 省名称、境外输入、日期、确诊(累计)人数、治愈人数、死亡人数、新增人数
    # sql = "SELECT year_id,format_date from date_calendar_full_scale where format_date <= '"+end_date+"' and format_date >= '"+start_date+"' ORDER BY format_date"
    sql = "SELECT y_date from date_calendar where y_date <= '"+end_date+"' and y_date >= '"+start_date+"' ORDER BY y_date";
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    db.commit()
    db.close()
    return result


# 星座日数据入库
def insert_data_cons_day(data):
    db = pymysql.connect(host=host, user='root', password=password, port=port, db='traffic')
    cursor = db.cursor()
    sql = 'insert into date_constellation_info_day(`constellation`,`con_date`,`com_fortune_index`,`love_fortune_index`,' \
          '`career_index`,`wealth_index`,`health_index`,`negotiation_index`,`lucky_color`,`lucky_number`,' \
          '`speed_dating_constellation`,`short_comment`,`com_fortune`,`love_fortune`,`career_fortune`,`wealth_fortune`,' \
          '`health_fortune`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
    cursor.execute(sql, data)
    cursor.close()
    db.commit()
    db.close()
    print("mysql-插入成功！\n")


# 星座周数据入库
def insert_data_cons_week(data):
    db = pymysql.connect(host=host, user='root', password=password, port=port, db='traffic')
    cursor = db.cursor()
    sql = 'insert into date_constellation_info_wmy(`constellation`,`con_date`,`com_fortune_index`,`love_fortune_index`,' \
          '`career_index`,`wealth_index`,`health_index`,`lucky_color`,`lucky_constellation`,' \
          '`beware_constellation`,`short_comment`,`com_fortune`,`love_fortune`,`career_fortune`,`wealth_fortune`,' \
          '`health_fortune`,`date_level`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
    cursor.execute(sql, data)
    cursor.close()
    db.commit()
    db.close()
    print("mysql-插入成功！\n")


# 星座月数据入库
def insert_data_cons_month(data):
    db = pymysql.connect(host=host, user='root', password=password, port=port, db='traffic')
    cursor = db.cursor()
    sql = 'insert into date_constellation_info_wmy(`constellation`,`con_date`,`com_fortune_index`,`love_fortune_index`,' \
          '`career_index`,`wealth_index`,`health_index`,`short_comment`,`com_fortune`,`love_fortune`,`career_fortune`,' \
          '`wealth_fortune`,`health_fortune`,`reduced_pressure`,`get_luck_way`,`date_level`) values (%s,%s,%s,%s,%s,' \
          '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
    cursor.execute(sql, data)
    cursor.close()
    db.commit()
    db.close()
    print("mysql-插入成功！\n")


# 星座年数据入库
def insert_data_cons_year(data):
    db = pymysql.connect(host=host, user='root', password=password, port=port, db='traffic')
    cursor = db.cursor()
    sql = 'insert into date_constellation_info_wmy(`constellation`,`con_date`,`com_fortune_index`,`love_fortune_index`,' \
          '`career_index`,`wealth_index`,`health_index`,`short_comment`,`com_fortune`,`love_fortune`,`career_fortune`,' \
          '`wealth_fortune`,`health_fortune`,`get_luck_way`,`date_level`) values (%s,%s,%s,%s,%s,' \
          '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
    cursor.execute(sql, data)
    cursor.close()
    db.commit()
    db.close()
    print("mysql-插入成功！\n")


# 星座详情码表入库
def insert_data_constellation_detail_info(data):
    db = pymysql.connect(host=host, user='root', password=password, port=port,db='traffic')
    cursor = db.cursor()
    sql = 'insert into date_constellation_detail_info(`constellation`,`date_range`,`cons_features`,`four_image_attributes`,' \
          '`palace`,`yin_yang_attributes`,`biggest_features`,`supervisor_plant`,`lucky_color`,`auspicious_items`,`lucky_number`,' \
          '`lucky_metal`,`performance`,`advantage`,`disadvantage`,`basic_traits`,`specific_traits`,`acting_style`,`blind_spot`,' \
          '`summary`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
    cursor.execute(sql, data)
    cursor.close()
    db.commit()
    db.close()
    print("mysql-插入成功！\n")


# 插入日历
def insert_data_calendar(data):
    db = pymysql.connect(host=host, user='root', password=password, port=port, db='traffic')
    cursor = db.cursor()
    sql = 'insert into date_calendar(`y_date`,`lunar`,`week`,`solar_terms`,`gregorian_calendar`) values (%s,%s,%s,%s,%s);'
    cursor.executemany(sql, data)
    cursor.close()
    db.commit()
    db.close()
    print("mysql-插入成功！\n")


# 插入当日的疫情状况 --- 国内
def insert_current_epidemic_internal(data):
    db = pymysql.connect(host=host, user='root', password=password, port=port, db='epidemic')
    cursor = db.cursor()
    sql = 'REPLACE INTO epi_current_detail(`date_today`,`curr_time`,`existing_diagnosis`,`ed_compare_yesterday`,`asymptomatic`,' \
          '`at_compare_yesterday`,`suspected`,`se_compare_yesterday`,`existing_critical_illness`, `eci_compare_yesterday`,' \
          '`cumulative_diagnosis`,`cdi_compare_yesterday`,`import_abroadz`,`ia_compare_yesterday`,`cumulative_cure`,`cc_compare_yesterday`,' \
          '`cumulative_deaths`,`cde_compare_yesterday`,`foreign_or_internal`,`create_time`,`update_time`)' \
          'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
    cursor.execute(sql, data)
    cursor.close()
    db.commit()
    db.close()
    print("mysql-插入成功！\n")


# 插入当日的疫情状况 ---  国外
def insert_current_epidemic_foreign(data):
    db = pymysql.connect(host=host, user='root', password=password, port=port, db='epidemic')
    cursor = db.cursor()
    sql = 'REPLACE INTO epi_current_detail(`date_today`,`curr_time`,`existing_diagnosis`,`ed_compare_yesterday`,' \
          '`cumulative_diagnosis`,`cdi_compare_yesterday`,`cumulative_cure`,`cc_compare_yesterday`,' \
          '`cumulative_deaths`,`cde_compare_yesterday`,`foreign_or_internal`,`create_time`,`update_time`)' \
          'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
    cursor.execute(sql, data)
    cursor.close()
    db.commit()
    db.close()
    print("mysql-插入成功！\n")


# 插入国内疫情的历史数据
def insert_internal_province_data(data):
    db = pymysql.connect(host=host, user='root', password=password, port=port, db='epidemic')
    cursor = db.cursor()
    # 省名称、市名称（省的话，就还是使用省名称）、日期、确诊(累计)人数、治愈人数、死亡人数、新增人数
    sql = 'REPLACE INTO epi_internal(`date_today`,`province_name`,`city_name`,`cumulative_diagnosis`,' \
          '`cumulative_cure`,`cumulative_deaths`,`new_add`,`existing_diagnosis`,`create_time`,`update_time`) ' \
          'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
    cursor.executemany(sql, data)
    cursor.close()
    db.commit()
    db.close()
    print("mysql-插入成功！\n")


# 插入国外疫情的历史数据
def insert_foreign_data(data):
    db = pymysql.connect(host=host, user='root', password=password, port=port, db='epidemic')
    cursor = db.cursor()
    # 国家名称、日期、确诊(累计)人数、治愈人数、死亡人数、新增人数
    sql = 'REPLACE INTO epi_foreign(`date_today`,`country_name`,`cumulative_diagnosis`,' \
          '`cumulative_cure`,`cumulative_deaths`,`new_add`,`existing_diagnosis`,`create_time`,`update_time`) ' \
          'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);'
    cursor.executemany(sql, data)
    cursor.close()
    db.commit()
    db.close()
    print("mysql-插入成功！\n")


# 插入国内省市的当日数据疫情的数据
def insert_internal_cur_day_data(data):
    db = pymysql.connect(host=host, user='root', password=password, port=port,db='epidemic')
    cursor = db.cursor()
    # 省名称、市名称（省的话，就还是使用省名称）、日期、确诊(累计)人数、治愈人数、死亡人数、新增人数
    # 省名称、市名称（省的话，就还是使用省名称）、日期、确诊(累计)人数、治愈人数、死亡人数、新增人数
    sql = 'REPLACE INTO epi_internal(`date_today`,`province_name`,`city_name`,`new_add`,' \
          '`existing_diagnosis`,`cumulative_diagnosis`,`cumulative_cure`,`cumulative_deaths`,`create_time`,`update_time`) ' \
          'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
    cursor.executemany(sql, data)
    cursor.close()
    db.commit()
    db.close()
    print("mysql-插入成功--国内省数据！\n")


# 将每日数据前面添加一个area_id
def insert_internal_cur_day_data_add_areaId():
    db = pymysql.connect(host=host, user='root', password=password, port=port, db='epidemic')
    cursor = db.cursor()
    # 省名称、市名称（省的话，就还是使用省名称）、日期、确诊(累计)人数、治愈人数、死亡人数、新增人数
    # 省名称、市名称（省的话，就还是使用省名称）、日期、确诊(累计)人数、治愈人数、死亡人数、新增人数
    sql = 'REPLACE INTO epi_internal_dim ( `area_id`, `date_today`, `province_name`, `city_name`, `new_add`, ' \
          '`existing_diagnosis`, `cumulative_diagnosis`, `cumulative_cure`, `cumulative_deaths`, `create_time`,' \
          ' `update_time` ) SELECT dim.area_id, epi.date_today, epi.province_name, epi.city_name, epi.new_add,' \
          ' epi.existing_diagnosis, epi.cumulative_diagnosis, epi.cumulative_cure, epi.cumulative_deaths, epi.create_time,' \
          ' epi.update_time' \
          ' FROM epi_internal epi LEFT JOIN pro_city_area_dim dim ' \
          'ON epi.province_name = dim.province AND epi.city_name = dim.area'
    cursor.execute(sql)
    cursor.close()
    db.commit()
    db.close()
    print("mysql-插入成功！\n")


# 插入疫情小区数据
def insert_community_data(data):
    db = pymysql.connect(host=host, user='root', password=password, port=port, db='epidemic')
    cursor = db.cursor()
    sql = 'REPLACE INTO epi_community(`date_today`,`province`,`city`,`district`,`street`,`middle_address`,`community`,' \
          '`show_address`,`full_address`,`lng`,`lat`,`cnt_sum_certain`,`release_date`,`create_time`,`update_time`,`location`) ' \
          'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,ST_GEOMFROMTEXT (%s));'
    cursor.executemany(sql, data)
    cursor.close()
    db.commit()
    db.close()
    print("mysql-插入成功！\n")


# 插入境外输入的数据
def insert_import_abroad(data):
    db = pymysql.connect(host=host, user='root', password=password, port=port, db='epidemic')
    cursor = db.cursor()
    # 省名称、境外输入、日期、确诊(累计)人数、治愈人数、死亡人数、新增人数
    sql = 'REPLACE INTO epi_import_abroad(`date_today`,`province_name`,`class_name`,`new_add`,' \
          '`existing_diagnosis`,`cumulative_diagnosis`,`cumulative_cure`,`cumulative_deaths`,`create_time`,`update_time`) ' \
          'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
    cursor.executemany(sql, data)
    cursor.close()
    db.commit()
    db.close()
    print("mysql-插入成功--境外输入数据！\n")


#  获取县区的信息
def select_area():
    db = pymysql.connect(host=host, user='root', password=password, port=port, db='epidemic')
    cursor = db.cursor()
    # 省名称、境外输入、日期、确诊(累计)人数、治愈人数、死亡人数、新增人数
    sql = 'SELECT area from epidemic.pro_city_area_dim;'
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    db.commit()
    db.close()
    return result
