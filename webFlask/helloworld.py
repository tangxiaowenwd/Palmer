# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/6/28 21:08
from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "<h1>Hello World</h1>"

if __name__ == '__main__':
    print('dd',__name__)
    app.run()