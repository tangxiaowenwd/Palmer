# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/9/30 22:30
import numpy as np
class Statistics():
    def __init__(self):
        pass


#协方差
def covariation(df):
    """
        计算两只股票的协方差：
            均值：
            离差：
    """
    ave1 = np.mean()
    ave2 = np.mean()
    dev1 = df["close"] - ave1
    dev2 = df["close"] - ave2

    cov = np.mean(dev1 * dev2)