from django.shortcuts import render
from django.http import HttpResponse,Http404
# Create your views here.
import tushare as ts
pro = ts.pro_api("d9f49767544519208fbf91e00a109558fe92e84bdcb70c9173144c24")

import pandas as pd

from .models import Stock,StockDetail,getModel
from django.db.models import Sum

def index(request):
    industrys = list(set(Stock.objects.all().values_list('industry')))
    industrys = [i[0] for i in industrys]
    #ss = StockDetail.objects.all()
    #reg = StockDetail.objects.values('net_mf_vol').annotate(number=Sum())
    return render(request,"index.html",locals())

def detail(request,industry):
    arg = request.GET.get("order_by")
    if arg:
        if industry == "all_infos":
            ary1 = StockDetail.objects.all().order_by(arg)
            return render(request, "detail.html", locals())
        ary1 = StockDetail.objects.filter(industry=industry).order_by(arg)
        if ary1:
            return render(request, "detail.html", locals())
        return render(request,"detail.html",{"industry":industry})
    else:
        if industry == "all_infos":
            ary1 = StockDetail.objects.all()
            return render(request, "detail.html", locals())
        ary1 = StockDetail.objects.filter(industry=industry)
        if ary1:
            return render(request, "detail.html", locals())
        return render(request,"detail.html",{"industry":industry})



def code(request,ts_code):
    code = "ts"+ts_code.split(".")[0]
    try:
        det = getModel(code).objects.all()
        infos = det[0]
        return render(request, "code.html", locals())
    except:
        raise Http404('Requested user not found.')

def manager(request,ts_code):
    return HttpResponse("管理页面")