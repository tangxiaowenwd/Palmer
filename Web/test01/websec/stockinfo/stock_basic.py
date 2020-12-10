# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/11/1 15:08
import tushare as ts
import datetime
import pandas as pd
from sqlalchemy import create_engine

writer = pd.ExcelWriter('./stock.xlsx')
conn = create_engine("mysql+pymysql://root:admin@localhost:3306/django?charset=utf8")
pro = ts.pro_api("d9f49767544519208fbf91e00a109558fe92e84bdcb70c9173144c24")
data = pro.query('stock_basic', exchange='', list_status='L',
                 fields='ts_code,name,area,industry,list_date,market,is_hs')


def get_weekly(days=5):
    day_list = []
    now = datetime.datetime.now()
    n = 0
    while len(day_list) < days:
        if n != 0:
            delta = datetime.timedelta(days=1)
            now = now - delta
        if now.weekday() != 5 and now.weekday() != 6:
            dt = now.strftime("%Y%m%d")
            day_list.append(dt)
        n += 1
    return day_list


def get_day():
    now = datetime.datetime.now()
    if now.weekday() != 5 and now.weekday() != 6:
        return now.strftime("%Y%m%d")
    while True:
        delta = datetime.timedelta(days=1)
        now = now - delta
        if now.weekday() != 5 and now.weekday() != 6:
            dt = now.strftime("%Y%m%d")
            return dt

# 按照产业排序
data = data.sort_values("industry")


def merge_data(dt):
    data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,name,area,industry,list_date,market,is_hs')

    # 设置最新日期
    data.set_index('ts_code')
    data.to_sql("stock", conn, index=False, if_exists='replace')

merge_data(get_day())
