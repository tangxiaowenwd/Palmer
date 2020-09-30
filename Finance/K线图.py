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
        mp.plot(self.dates, df["close"], color="black", label=self.name, linestyle="-", linewidth=1, alpha=0.3)

        #self.K_line()
        # self.Mean_line()
        # self.Monvolve()
        # self.Mean_move_line()
        # self.Bulindai()

        self.line_p()

        mp.plot()
        mp.legend()
        mp.gcf().autofmt_xdate()
        mp.show()

    def line_p(self):
    #     A = np.zeros((3,3))
    #     for j in range(3):
    #         A[j,] = self.df["close"][j:j+3]
    #     B = self.df["close"][3:6]
    #     x = np.linalg.lstsq(A,B)[0]
    #     print(x)
    #     print(B.dot(x))
    #     print(self.df["close"][6])
        trends = (self.df["high"]+self.df["low"] + self.df["close"]) / 3
        mp.scatter(self.dates,trends,marker="o",color="red",s=30,label="trends")
        A = np.ones(self.df["close"].size)
        days = self.dates.astype('M8[D]').astype('int32')
        A = np.column_stack((days,np.ones_like(days)))
        x = np.linalg.lstsq(A,self.df["close"])[0]
        tr = x[0]*days+x[1]
        mp.plot(self.dates,tr,color='green')




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
        if weight:
            # 加权卷积运算
            x = np.linspace(0,1,days)
            kernel1 =np.exp(x)
            kernel1=kernel1/kernel1.sum()
            print(kernel1)
            sma53 = np.convolve(self.df["close"], kernel1, 'valid')
            mp.plot(self.dates[:-(days-1)], sma53, color='orange', label="加权卷积_5", linestyle="--", linewidth=2, alpha=0.9)
        else:
            # 卷积运算
            kernel = np.ones(days) / days
            sma52 = np.convolve(self.df["close"], kernel, 'valid')
            mp.plot(self.dates[:-(days-1)], sma52, color='green', label="卷积_5", linestyle="--", linewidth=2, alpha=0.9)

    def Bulindai(self,days=10):
        kernel = np.ones(days) / days
        sma52 = np.convolve(self.df["close"], kernel, 'valid')
        mp.plot(self.dates[:-(days-1)], sma52, color='green', label="卷积_5", linestyle="--", linewidth=1, alpha=0.5)
        stds = np.zeros(sma52.size)
        for i in range(stds.size):
            stds[i] = self.df["close"][i:i+days].std()
        upper = sma52 + 2 * stds
        lower = sma52 - 2 * stds
        mp.plot(self.dates[:-(days-1)],upper,color='red',label="Upper")
        mp.plot(self.dates[:-(days-1)], lower, color='red', label="Lower")
        mp.fill_between(self.dates[:-(days-1)],upper,lower,lower<upper,color='orangered',alpha=0.2)



class GetInfo():
    def __init__(self,ts_code):
        self.pro = ts.pro_api("d9f49767544519208fbf91e00a109558fe92e84bdcb70c9173144c24")
        self.ts_code = ts_code

    def get_info(self):
        data = self.pro.query('stock_basic', exchange='', list_status='L',
                         fields='ts_code,symbol,name,area,industry,list_date')
        #data.to_excel("ts_code.xls")
        code_info = data[data["ts_code"]==self.ts_code]
        # if not code_info.bool():
        #     raise Exception("没有找到%s得相关信息" %self.ts_code)
        name = self.convert_str(code_info["name"])
        return name

    def convert_str(self,strs):
        regex = re.compile("\s+")
        name = regex.split(str(strs).split("\n")[0])[1]
        return name


    def main(self):
        df = self.pro.query('daily', ts_code=self.ts_code)[:60]
        name = self.get_info()
        return name,df


class StatistacalIndex():
    def __init__(self):
        pass





if __name__ == "__main__":
    main = GetInfo(ts_code="600519.SH")
    name,df = main.main()
    Graphic(df,name)