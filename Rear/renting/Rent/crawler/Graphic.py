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
from Rent.crawler.BasicInfo import GetInfo

def Grasphic(ts_code):
    name, df = GetInfo(ts_code).main()
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
    mp.plot(    dates, df["close"], color = "black", label = name, linestyle = "-", linewidth = 1, alpha = 0.5)
    # for i in params:
    #     if i == "K":
    #         K_line(df,dates)
    regression(df,dates)
    Mean_move_line(df,dates)
    bulindai(df,dates)
    mp.legend()
    mp.gcf().autofmt_xdate()
    # mp.show()
    mp.savefig("E:\Github\Palmer\Rear\\renting\Rent\static\images\\1.jpg")

def bulindai(df,dates,days=5):
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
    #填充布林带
    mp.fill_between(dates[days:], upper, lower, lower < upper, color="orangered", alpha=0.05)

def K_line(df,dates):
    # #绘制K线图
    rise = df['close'] > df['open']
    color = ["white" if x else 'green' for x in rise]
    ecolor = ["red" if x else 'green' for x in rise]
    mp.bar(dates, df['change'], width=0.8, bottom=df["open"], color=color, edgecolor=ecolor, zorder=3)
    # 绘制影线
    mp.vlines(dates, df['low'], df['high'], color=ecolor)


def Mean_line(df,dates):
    # 算术平均值：当前一组数据无偏估计
    mean = np.mean(df["close"])
    print("算术平均值为：", mean)
    mp.hlines(mean, dates[0], dates[-1], color='blue', label="mean", linestyles=":", alpha=0.5)


def Mean_move_line(df,dates,days=5, weight=False):
    # 移动均线
    ma5 = np.zeros(df['close'].size - days)
    for i in range(ma5.size):
        data = df['close'][i:i + days]
        ma5[i] = data.mean()
    mp.plot(dates[days:], ma5, color='blue', label="Mean-5", linestyle="--", linewidth=2, alpha=0.8)


def Monvolve(df,dates,days=5, weight=False):
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
        mp.plot(dates[days - 1:],sma52, color='green', label="卷积_5", linestyle="--", linewidth=2, alpha=0.9)

def regression(df,dates,days=5):
    """
        回归运算
    """
