#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Time    : 2020/9/26 17:23
# Author  : TangXiaowen
import tushare as ts
import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
import matplotlib.dates as md
import re
from sklearn.linear_model import logistic
import sklearn

pro = ts.pro_api("d9f49767544519208fbf91e00a109558fe92e84bdcb70c9173144c24")




class GetInfo():
    def __init__(self,ts_code):
        self.pro = ts.pro_api("d9f49767544519208fbf91e00a109558fe92e84bdcb70c9173144c24")
        self.ts_code = ts_code

    """
        返回：name,df[四元素]
    """
    def get_stock_info(self):
        data = self.pro.fund_daily(ts_code=self.ts_code)
        code_info = data[data["ts_code"] == self.ts_code]
        name = self.convert_str(code_info["name"])
        return name

    def convert_str(self, strs):
        regex = re.compile("\s+")
        name = regex.split(str(strs).split("\n")[0])[1]
        return name

    def get_all_fund(self, market):
        data = self.pro.fund_basic(market=market)
        # da[da["name"].str.contains("白酒")]
        df = data[data["ts_code"] == self.ts_code]
        name = self.convert_str(df["name"])
        res = self.pro.fund_daily(ts_code=self.ts_code)
        return res, name

    def main(self, days=60):
        """
        days:默认的天数
        """
        if self.ts_code.split(".")[1] == "SZ":  # 场外基金
            df, name = self.get_all_fund(market="E")
        if self.ts_code.split(".")[1] == "OF":  # 场内基金
            df, name = self.get_all_fund(market="E")
        if self.ts_code.split(".")[1] == "SH":  # 股票
            df, name = self.get_all_fund(market="E")
        return name, df[:days]


def Grasphic(ts_code):
    name, df = GetInfo(ts_code).main()
    print(name)
    df = df[::-1]
    dates = np.array(pd.to_datetime(df["trade_date"], errors="ignore"))
    mp.rcParams['font.family'] = ['sans-serif']
    mp.rcParams['font.sans-serif'] = ['SimHei']
    mp.title(name)
    mp.xlabel("Date", fontsize=14)
    mp.ylabel("closing price", fontsize=14)
    mp.grid(linestyle=":")
    # 拿到坐标抽
    ax = mp.gca()
    # 设置主刻度定位器为周定位器（每周显示主刻度文本）
    ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
    ax.xaxis.set_major_formatter(md.DateFormatter('%d-%m-%Y'))
    mp.plot(dates, df["close"], color="black", label=name, linestyle="-", linewidth=1, alpha=0.5)
    # for i in params:
    #     if i == "K":
    #         K_line(df,dates)
    regression(df, dates)
    Mean_move_line(df, dates)
    bulindai(df, dates)
    mp.legend()
    mp.gcf().autofmt_xdate()
    mp.show()


def bulindai(df, dates, days=5):
    ma5 = np.zeros(df['close'].size - days)
    for i in range(ma5.size):
        data = df['close'][i:i + days]
        ma5[i] = data.mean()
    mp.plot(dates[days:], ma5, color='blue', label="Mean-5", linestyle="--", linewidth=2, alpha=0.8)
    stds = np.zeros(ma5.size)
    for i in range(stds.size):
        stds[i] = df["close"][i: i + 5].std()  # 计算标准差
    upper = ma5 + 2 * stds  # 计算上轨
    lower = ma5 - 2 * stds  # 计算下轨
    mp.plot(dates[days:], upper, color="green", label="UPPER")
    mp.plot(dates[days:], lower, color="blue", label="LOWER")
    # 填充布林带
    mp.fill_between(dates[days:], upper, lower, lower < upper, color="orangered", alpha=0.05)

def K_line(df, dates):
    # #绘制K线图
    rise = df['close'] > df['open']
    color = ["white" if x else 'green' for x in rise]
    ecolor = ["red" if x else 'green' for x in rise]
    mp.bar(dates, df['change'], width=0.8, bottom=df["open"], color=color, edgecolor=ecolor, zorder=3)
    # 绘制影线
    mp.vlines(dates, df['low'], df['high'], color=ecolor)


def Mean_line(df, dates):
    # 算术平均值：当前一组数据无偏估计
    mean = np.mean(df["close"])
    print("算术平均值为：", mean)
    mp.hlines(mean, dates[0], dates[-1], color='blue', label="mean", linestyles=":", alpha=0.5)


def Mean_move_line(df, dates, days=5, weight=False):
    # 移动均线
    ma5 = np.zeros(df['close'].size - days)
    for i in range(ma5.size):
        data = df['close'][i:i + days]
        ma5[i] = data.mean()
    mp.plot(dates[days:], ma5, color='blue', label="Mean-5", linestyle="--", linewidth=2, alpha=0.8)


def Monvolve(df, dates, days=5, weight=False):
    """
    卷积
    """
    if weight:
        # 加权卷积运算
        x = np.linspace(0, 1, days)
        kernel1 = np.exp(x)
        kernel1 = kernel1 / kernel1.sum()
        print(kernel1)
        sma53 = np.convolve(df["close"], kernel1, 'valid')
        mp.plot(dates[days - 1:], sma53, color='orange', label="加权卷积_5", linestyle="--", linewidth=2,
                alpha=0.9)
    else:
        # 卷积运算
        kernel = np.ones(days) / days
        sma52 = np.convolve(df["close"], kernel, 'valid')
        mp.plot(dates[days - 1:], sma52, color='green', label="卷积_5", linestyle="--", linewidth=2, alpha=0.9)


def get_all_funds():
    data = pro.fund_basic(market="E").append(pro.fund_basic(market="O"))
    return data

def get_all_fund_name():
    df = get_all_funds()
    name = [x for x in zip(df["name"],df["ts_code"])]
    return name

def get_buy_info():
    pass

def get_sale_info():
    pass

def convert_str(self, strs):
    regex = re.compile("\s+")
    name = regex.split(str(strs).split("\n")[0])[1]
    return name



import sklearn.linear_model as lm
def regression():
    """
        线性回归运算
    """
    #创建模型
    mp.rcParams['font.family'] = ['sans-serif']
    mp.rcParams['font.sans-serif'] = ['SimHei']
    mp.xlabel("Date", fontsize=14)
    mp.ylabel("closing price", fontsize=14)
    # 拿到坐标抽
    ax = mp.gca()
    # 设置主刻度定位器为周定位器（每周显示主刻度文本）
    ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
    ax.xaxis.set_major_formatter(md.DateFormatter('%d-%m-%Y'))
    res = pro.fund_daily(ts_code="159808.SZ")[::-1]
    x = np.array(res[["trade_date","open","high","low"]])
    print(x)

    y = np.array(res["close"])
    model = lm.LinearRegression()
    model.fit(x,y.reshape(-1,1))
    pred_y = model.predict(np.array(["20200931",0.95,0.96,0.97]).reshape(-1, 1))
    print(pred_y)
    mp.grid(linestyle=":")
    mp.plot(x,y)
    mp.scatter("20200931", pred_y,color="red",s=10)
    mp.legend()
    mp.gcf().autofmt_xdate()
    mp.show()






#傅里叶变换



