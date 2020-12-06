#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Time    : 2020/12/1 22:43
# Author  : TangXiaowen

from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index,name="index"),
    path("detail/<str:ts_code>",views.detail,name="detail")
]
