from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import tushare as ts
pro = ts.pro_api("d9f49767544519208fbf91e00a109558fe92e84bdcb70c9173144c24")

import pandas as pd

from .models import Stock,Dayily


def index(request):
    ss = Dayily.objects.all()
    industrys = list(set(Dayily.objects.all().values_list('industry')))
    industrys = [i[0] for i in industrys]

    return render(request,"index.html",locals())

def detail(request,ts_code):
    ary1 = request.GET.get("industry")
    if ary1:
        return render(request, "index.html", locals())
    return render(request,"detail.html",{"ts_code":ts_code})


