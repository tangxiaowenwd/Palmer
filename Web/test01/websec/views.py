from django.shortcuts import render
from django.http import HttpResponse,Http404
# Create your views here.
import tushare as ts
pro = ts.pro_api("d9f49767544519208fbf91e00a109558fe92e84bdcb70c9173144c24")

import pandas as pd

from .models import Stock,StockDetail,getModel


def index(request):
    ss = Stock.objects.all()
    industrys = list(set(Stock.objects.all().values_list('industry')))
    industrys = [i[0] for i in industrys]
    return render(request,"index.html",locals())

def detail(request,industry):
    ary1 = Stock.objects.filter(industry=industry)
    print(ary1)
    if ary1:
        return render(request, "detail.html", locals())
    return render(request,"detail.html",{"industry":industry})



def code(request,ts_code):
    code = "ts"+ts_code.split(".")[0]
    try:
        det = getModel(code).objects.all()
        return render(request, "code.html", locals())
    except:
        raise Http404('Requested user not found.')

def manager(request,ts_code):
    return HttpResponse("管理页面")
