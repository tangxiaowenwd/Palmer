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
import re


#日期转换函数
def dmy2ymd(dmy):
    dmy = str(dmy,encoding='utf-8')

class Graphic():
    def __init__(self,df,name):
        self.df = df
        self.name = name
        self.dates = np.array(pd.to_datetime(self.df["trade_date"],errors="ignore"))
        mp.rcParams['font.family'] = ['sans-serif']
        mp.rcParams['font.sans-serif'] = ['SimHei']
        mp.figure(name,facecolor="lightgray")
        mp.title(self.name)
        mp.xlabel("Date",fontsize=14)
        mp.ylabel("closing price",fontsize=14)
        mp.grid(linestyle=":")
        #拿到坐标抽
        ax = mp.gca()
        #设置主刻度定位器为周定位器（每周显示主刻度文本）
        ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
        ax.xaxis.set_major_formatter(md.DateFormatter('%d-%m-%Y'))
        mp.plot(self.dates, df["close"], color="black", label=self.name, linestyle="-", linewidth=2, alpha=1)

        #self.K_line()
        self.Mean_line()
        self.Monvolve()
        self.Mean_move_line()

        mp.plot()
        mp.legend()
        mp.gcf().autofmt_xdate()
        mp.show()

    def K_line(self):
        # #绘制K线图
        rise = self.df['close'] > self.df['open']
        color = ["white" if x else 'green' for x in rise]
        ecolor = ["red" if x else 'green' for x in rise]
        mp.bar(self.dates,self.df['change'],width=0.8,bottom=self.df["open"],color=color,edgecolor=ecolor,zorder=3)
        #绘制影线
        mp.vlines(self.dates,self.df['low'],self.df['high'],color=ecolor)

    def Mean_line(self,):
        #算术平均值：当前一组数据无偏估计
        mean = np.mean(self.df["close"])
        print("算术平均值为：",mean)
        mp.hlines(mean,self.dates[0],self.dates[-1],color='blue',label="mean",linestyles=":",alpha=0.5)
    def Mean_move_line(self,days=10,weight=False):
        #移动均线
        ma5 = np.zeros(self.df['close'].size - days)
        for i in range(ma5.size):
            data = self.df['close'][i:i+days]
            ma5[i] = data.mean()
        mp.plot(self.dates[days:],ma5,color='blue',label="Mean-5",linestyle="--",linewidth=2,alpha=0.8)



    def Monvolve(self,days=5,weight=False):
        """
        卷积
        """
        if weight:
            # 加权卷积运算
            x = np.linspace(0,1,days)
            kernel1 =np.exp(x)
            kernel1=kernel1/kernel1.sum()
            print(kernel1)
            sma53 = np.convolve(self.df["close"], kernel1, 'valid')
            mp.plot(self.dates[days-1:], sma53, color='orange', label="加权卷积_5", linestyle="--", linewidth=2, alpha=0.9)
        else:
            # 卷积运算
            kernel = np.ones(days) / days
            sma52 = np.convolve(self.df["close"], kernel, 'valid')
            mp.plot(self.dates[days - 1:], sma52, color='green', label="卷积_5", linestyle="--", linewidth=2, alpha=0.9)
