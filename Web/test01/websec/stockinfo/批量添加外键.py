# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/12/13 11:53
import pymysql

conn = pymysql.connect(user='root',password='admin',database='django',host='127.0.0.1', port=3306)
cursor = conn.cursor()

#sql = "INSERT INTO news(title,summary,visits,accountName,grabTime) VALUES(%s,%s,%s,%s,%s)"
def con(sql):
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
    except Exception as e:
        conn.rollback()
    finally:
        conn.commit()
        cursor.close()
        conn.close()
    return data
data = con("show tables;")
ts_code = [i[0] for i in data if "ts" in i[0]]
for i in ts_code:
    sql = "ALTER TABLE %s ADD id integer AUTO_INCREMENT NOT NULL PRIMARY KEY FIRST; "%i
    print(sql)
