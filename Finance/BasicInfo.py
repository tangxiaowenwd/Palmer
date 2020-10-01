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
