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

def detail(request,industry):
    ary1 = Dayily.objects.filter(industry=industry)
    print(ary1)
    if ary1:
        return render(request, "detail.html", locals())
    return render(request,"detail.html",{"industry":industry})



def code(request,ts_code):
    return HttpResponse("<h1>%s</h1>"%ts_code)