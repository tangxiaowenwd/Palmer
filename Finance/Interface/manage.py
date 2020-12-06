# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/7/26 16:22
from flask import render_template, Blueprint,Flask,jsonify
from sqlalchemy import create_engine
import pandas as pd
import json

index_bp = Blueprint('index', __name__)

ad = ['ts_code', 'name', 'management', 'custodian', 'fund_type', 'found_date', 'due_date', 'list_date', 'issue_date', 'delist_date', 'issue_amount', 'm_fee', 'c_fee', 'duration_year', 'p_value', 'min_amount', 'exp_return', 'benchmark', 'status', 'invest_type', 'type', 'trustee', 'purc_startdate', 'redm_startdate', 'market']

class query():
    def __init__(self):
        self.engine = create_engine(
    "mysql+mysqlconnector://root:admin@localhost:3306/stock")
    def redata(self):
        sql = "select * from jijin;"
        df = pd.read_sql_query(sql, self.engine)
        return df
df = query().redata()

@index_bp.route('/')
def index():
    datas = {}
    a = 0
    for i in df[0:20].itertuples():
        td = {}
        for s in ad:
            td[s] = i.__getattribute__(s)
        datas[a] = td
        a += 1
    return render_template('index.html',datas= datas,columns = df.columns)


@index_bp.route('/dataAjax/<num>',methods=['POST','GET'])
def dataajax(num):
    num = int(num)*20
    datas = {}
    a = 0
    for i in df[num:num+20].itertuples():
        td = {}
        for s in ad:
            td[s] = i.__getattribute__(s)
        datas[a] = td
        a += 1
    return json.dumps({"ts_code":1,"name":"tang","price":"2"})

app = Flask(__name__,template_folder='templates',static_folder="static")
app.register_blueprint(index_bp)


if __name__=="__main__":
    app.run(debug=True)

