#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Time    : 2020/12/2 22:39
# Author  : TangXiaowen
from django import forms

class StockForm(forms.Form):
    ts_code = forms.CharField(label='stock', max_length=10)