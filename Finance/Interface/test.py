# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/8/22 12:13
import json
from flask import render_template, Blueprint,Flask,jsonify
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
index_bp = Blueprint('index', __name__)

engine = create_engine(
    "mysql+pymysql://root:admin@localhost:3306/stock?charset=UTF8MB4")
sql = "select * from jijin;"
df = pd.read_sql_query(sql, engine)
data = {}
ass = {}
ad = ['ts_code', 'name', 'management', 'custodian', 'fund_type', 'found_date', 'due_date', 'list_date', 'issue_date', 'delist_date', 'issue_amount', 'm_fee', 'c_fee', 'duration_year', 'p_value', 'min_amount', 'exp_return', 'benchmark', 'status', 'invest_type', 'type', 'trustee', 'purc_startdate', 'redm_startdate', 'market']
def dataajax():
    datas = {}
    a = 0
    for i in df[0:20].itertuples():
        td = {}
        for s in ad:
            td[s] = i.__getattribute__(s)
        datas[a] = td
        a += 1
    print(datas[0])
    for i in datas.keys():
        for s in datas[i]:
            print(datas[i][s])

if __name__=="__main__":
    dataajax()
