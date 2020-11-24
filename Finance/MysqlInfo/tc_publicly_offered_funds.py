# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/8/22 4:49
from Base import Base

import pandas as pd

class tc_publicly_offered_funds(Base):
    def get_df(self):
        get_data = self.pro.fund_basic(market='E').append(self.pro.fund_basic(market='O'))
        return self.data

    def to_mysql(self):

        self.get_df().to_sql(name='jijin', con=self.engine, if_exists='append',
                    index=False, index_label='id')
    def read_sql(self):
        sql = "select * from jijin;"
        df = pd.read_sql_query(sql, self.engine)
        print(df.head())




if __name__=="__main__":
    tc_publicly_offered_funds().read_sql()