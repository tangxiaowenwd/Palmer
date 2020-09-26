#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Time    : 2020/9/26 17:23
# Author  : TangXiaowen
import tushare as ts
import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md


#日期转换函数
def dmy2ymd(dmy):
    dmy = str(dmy,encoding='utf-8')


class Main():
    def __init__(self):
        self.pro = ts.pro_api("d9f49767544519208fbf91e00a109558fe92e84bdcb70c9173144c24")

    def main(self):
        df = self.pro.query('daily', ts_code='000005.SZ')[:40]
        print(df)
        df["trade_date"] = pd.to_datetime(df["trade_date"],errors="ignore")
        mp.figure("000001.SZ",facecolor="lightgray")
        mp.title("000001.SZ",fontsize=16)
        mp.xlabel("Date",fontsize=14)
        mp.ylabel("closing price",fontsize=14)
        mp.grid(linestyle=":")
        #拿到坐标抽
        ax = mp.gca()
        #设置主刻度定位器为周定位器（每周显示主刻度文本）
        ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
        ax.xaxis.set_major_formatter(md.DateFormatter('%d-%m-%Y'))
        #设置次定位器为日定位器
        #ax.xaxis.set_major_locator(md.DayLocator(md.DayLocator()))

        #整理颜色
        rise = df['close'] > df['open']
        color = ["white" if x else 'green' for x in rise]
        ecolor = ["red" if x else 'green' for x in rise]
        mp.plot(df["trade_date"],df["close"],color="red",label="000001.sz",linestyle="--",linewidth=2,alpha=0.3)

        #绘制K线图
        mp.bar(df["trade_date"],df['change'],width=0.8,bottom=df["open"],color=color,edgecolor=ecolor,zorder=3)
        #绘制影线
        mp.vlines(df['trade_date'],df['low'],df['high'],color=ecolor)

        mp.plot()
        mp.legend()
        mp.gcf().autofmt_xdate()
        mp.show()




if __name__ == "__main__":
    main = Main()
    main.main()