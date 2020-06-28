#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Time    : 2020/6/24 8:12
# Author  : TangXiaowen
import tushare as ts
from time import sleep
import datetime as dt


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
        return self.pro.fund_nav(ts_code=ts_code)


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

class Getyield ():
    def __int__(self,num=6):
        self.num = num

    def main(self):
        pass

    #单位净值日跌涨幅
    def DailyIncome(self,unit_nav):
        res = (unit_nav[0] - unit_nav[1]) / unit_nav[1]
        return "%.2f%%" %(res*100)

    #周收益
    def WeeklyYield(self,unit_nav):
        try:
            res = (unit_nav[0] - unit_nav[5]) / unit_nav[5]
            return "%.2f%%" % (res * 100)
        except:
            return None

    #月收益
    def MonthlyYield(self,unit_nav):
        try:
            res = (unit_nav[0] - unit_nav[21]) / unit_nav[21]
            return "%.2f%%" % (res * 100)
        except:
            return None

    #季度收益
    def QuarterlyYield(self,unit_nav):
        try:
            res = (unit_nav[0] - unit_nav[63]) / unit_nav[63]
            return "%.2f%%" % (res * 100)
        except:
            return None

    #年收益
    def AnnualYield(self,unit_nav):
        try:
            res = (unit_nav[0] - unit_nav[252]) / unit_nav[252]
            return "%.2f%%" % (res * 100)
        except:
            return None


    #3年收益和成立以来的收益
    def Annual3Yield(self,unit_nav):
        n = len(unit_nav)
        if n < 756:
            res = (unit_nav[0] - unit_nav[n-1]) / unit_nav[n-1]
            return [None,"%.2f%%" % (res * 100)]
        res = (unit_nav[0] - unit_nav[756]) / unit_nav[756]
        res1 = (unit_nav[0] - unit_nav[n-1]) / unit_nav[n-1]
        return ["%.2f%%" % (res * 100),"%.2f%%" % (res1 * 100)]


class Filter():
    """
    基金筛选
    """
    def __init__(self):
        self.pro = ts.pro_api("d9f49767544519208fbf91e00a109558fe92e84bdcb70c9173144c24")

    def getperformance(self,ts_code):
        performance = [ts_code]

        unit_nav = self.pro.fund_nav(ts_code=ts_code)["unit_nav"]
        if len(unit_nav) >= 252:
            performance.append(Getyield().DailyIncome(unit_nav))
            performance.append(Getyield().WeeklyYield(unit_nav))
            performance.append(Getyield().MonthlyYield(unit_nav))
            performance.append(Getyield().QuarterlyYield(unit_nav))
            performance.append(Getyield().AnnualYield(unit_nav))
            performance.extend(Getyield().Annual3Yield(unit_nav))
            print(performance)


if __name__ == "__main__":
    tss = GetTushare().get_fund_basic(market="E")
    for ts_code in tss["ts_code"]:
        main = Filter().getperformance(ts_code=ts_code)
        sleep(1)

