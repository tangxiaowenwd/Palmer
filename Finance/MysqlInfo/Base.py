# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/8/22 4:50
import tushare as ts
from sqlalchemy import create_engine

class Base():
    def __init__(self):
        self.pro = ts.pro_api("d9f49767544519208fbf91e00a109558fe92e84bdcb70c9173144c24")
        self.engine = create_engine(
            "mysql+pymysql://root:admin@localhost:3306/stock?charset=UTF8MB4")