#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Time    : 2020/6/24 8:12
# Author  : TangXiaowen
import tushare as ts

class GetTushare():
    def __init__(self):
        self.pro = ts.pro_api("d9f49767544519208fbf91e00a109558fe92e84bdcb70c9173144c24")


    def get_fund_basic(self,market="E"):
        """
        masket: E-场内  O-场外
        :return:
            invst_type:投资风格
            type:基金类型
            status:D-摘牌  I发行 L已上市
        """
        df = self.pro.fund_basic(market='O')
        return df

    #基金公司
    def get_fund_company(self):
        return self.pro.fund_company()

    #基金经理
    def get_fund_manager(self,ts_code):
        # 单只基金
        df = self.pro.fund_manager(ts_code=ts_code)
        # 多只基金
        df = self.pro.fund_manager(ts_code=ts_code)

    #基金净值
    def get_fund_nav(self,ts_code):
        self.pro.fund_nav(ts_code)

    #基金持仓
    def get_fund_portfolio(self,ts_code):
        df = self.pro.fund_portfolio(ts_code=ts_code)

    #基金规模
    def get_fund_share(self,ts_code):
        # 单只基金
        df = self.pro.fund_share(ts_code=ts_code)
        # 多只基金
        df = self.pro.fund_share(ts_code=ts_code)

    #基金分红
    def get_fund_div(self,ts_code):
        df = self.pro.fund_div(ann_date='20181018')

    #场内基金日线行情
    def get_fund_daily(self,ts_code):
        df = self.pro.fund_daily(ts_code=ts_code, start_date='20180101', end_date='20181029')

    #复权因子
    def get_fund_adj(self,ts_code):
        df = self.pro.fund_adj(ts_code=ts_code, start_date='20190101', end_date='20190926')

    def main(self):
            pass

class GetInfo():
    def __init__(self):
        self.Tushare = GetTushare()

    def get_ts_code(self):
        """

        :return: Series对象
        """
        df = self.Tushare.get_fund_basic()
        return df["ts_code"]

def get50():
    main = GetInfo()
    fund = GetTushare()
    ss = main.get_ts_code()
    for s in ss[:20]:
        #场内场外分开获取
        print(s)
        res = fund.get_fund_nav(ts_code=s) #获取基金净值
        #根据日期获取最近孻
        print(res)




if __name__ == "__main__":
    main = GetTushare()
    for i in main.get_fund_basic()["ts_code"]:
        main.get_fund_nav(ts_code=i)




