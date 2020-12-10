from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Stock,Dayily

class StockAdmin(admin.ModelAdmin):
    pass

class DayilyAdmin(admin.ModelAdmin):
    #site_url = "/to"


    '''设置列表可显示的字段'''
    list_display = ('market','ts_code','trade_date','name','industry', 'open','high','low','close','pre_close','change','pct_chg','volume_ratio','turnover_rate','pe','total_mv')

    '''设置过滤选项'''
    list_filter = ('industry',)

    '''每页显示条目数'''
    list_per_page = 50

    '''设置可编辑字段'''
    #list_editable = ('name',)

    '''按日期月份筛选'''
    # date_hierarchy = 'pub_date'

    '''按发布日期排序'''
    ordering = ('-pct_chg',)

    # 由于Django admin默认的多对多关系(ManyToMany)选择器是复选框，非常的不好用。一个更好的方法是使用filter_horizontal或filter_vertical选项filter_horizontal


admin.site.register(Stock, StockAdmin)
admin.site.register(Dayily, DayilyAdmin)
