# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/7/26 16:25
from flask import Blueprint
from flask import render_template
from manage import app


#error_bp = Blueprint('error', __name__)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error/404.html"), 404
