# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/11/1 15:08
import tushare as ts
import datetime
import pandas as pd
from sqlalchemy import create_engine

#writer = pd.ExcelWriter('./stock.xlsx')
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
    while True:
        delta = datetime.timedelta(days=1)
        now = now - delta
        if now.weekday() != 5 and now.weekday() != 6:
            dt = now.strftime("%Y%m%d")
            return dt

# 按照产业排序
data = data.sort_values("industry")


def merge_data(ts_code):
    day_data = pro.daily(ts_code=ts_code)[
        ["ts_code", "trade_date", "open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol", "amount"]]
    dayily = pro.daily_basic(ts_code=ts_code,
                             fields='ts_code,trade_date,turnover_rate,volume_ratio,pe,pb,ps,dv_ratio,total_share,float_share,free_share,total_mv,circ_mv')
    moneyflow = pro.moneyflow(ts_code=ts_code)[
        ["ts_code","trade_date", "buy_sm_vol", "buy_sm_amount", "sell_sm_vol", "sell_sm_amount", "buy_md_vol", "buy_md_amount",
         "sell_md_vol", "sell_md_amount", "buy_lg_vol",
         "buy_lg_amount", "sell_lg_vol", "sell_lg_amount", "buy_elg_vol", "buy_elg_amount", "sell_elg_vol",
         "sell_elg_amount", "net_mf_vol", "net_mf_amount"]]

    #a = pd.merge(data, day_data, how='inner', on='ts_code')
    a1 = pd.merge(day_data, dayily, how='inner', on='trade_date')
    a2 = pd.merge(a1, moneyflow, how='inner', on='trade_date')

    # 设置最新日期
    day_data.set_index('ts_code')
    #a2.to_excel(writer, sheet_name=dt, index=0)
    a2.to_sql("ts"+str(ts_code.split(".")[0]), conn, index=True, if_exists='replace')


for ts_code in list(data["ts_code"]):
    merge_data(ts_code)

# writer.save()
# writer.close()
