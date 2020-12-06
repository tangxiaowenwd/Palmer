# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/7/26 16:25
from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/login")
def login():
    return "<h1>你好</h1>"

@auth_bp.route("/register")
def register():
    return "<h1>注册</h1>"

