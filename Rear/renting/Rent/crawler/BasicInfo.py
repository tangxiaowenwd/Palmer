# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/9/30 22:24
import tushare as ts
import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md
import re

class GetInfo():
    def __init__(self,ts_code):
        self.pro = ts.pro_api("d9f49767544519208fbf91e00a109558fe92e84bdcb70c9173144c24")
        self.ts_code = ts_code
    """
        返回：name,df[四元素]
    """
    def get_all_funds(self):
        data = self.pro.fund_basic(market="E")

    def get_stock_info(self):
        data = self.pro.fund_daily(ts_code=self.ts_code)
        code_info = data[data["ts_code"]==self.ts_code]
        name = self.convert_str(code_info["name"])
        return name

    def convert_str(self,strs):
        regex = re.compile("\s+")
        name = regex.split(str(strs).split("\n")[0])[1]
        return name

    def get_all_fund(self,market):
        data = self.pro.fund_basic(market=market)
        # da[da["name"].str.contains("白酒")]
        df = data[data["ts_code"] == self.ts_code]
        name = self.convert_str(df["name"])
        res = self.pro.fund_daily(ts_code=self.ts_code)
        return res,name

    def main(self,days=60):
        """
        days:默认的天数
        """
        if self.ts_code.split(".")[1] == "SZ": #场外基金
            df,name = self.get_all_fund(market="E")
            print(df)
        if self.ts_code.split(".")[1] == "OF": #场内基金
            df, name = self.get_all_fund(market="E")
        if self.ts_code.split(".")[1] == "SH": #股票
            df, name = self.get_all_fund(market="E")
        return name,df[:days]
