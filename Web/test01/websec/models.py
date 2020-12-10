from django.db import models


# Create your models here.


# 股票列表
class Stock(models.Model):
    ts_code = models.CharField(max_length=10, blank=True, primary_key=True, verbose_name="股票代码")
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name="股票名称")
    area = models.CharField(max_length=50, blank=True, null=True, verbose_name="所在地域")
    industry = models.CharField(max_length=20, blank=True, null=True, verbose_name="所属行业")
    list_date = models.CharField(max_length=20, blank=True, null=True, verbose_name="上市日期")
    market = models.CharField(max_length=20, blank=True, null=True, verbose_name="市场类型")
    is_hs = models.CharField(max_length=20, blank=True, null=True, verbose_name="是否沪深港通标的")

    class Meta:
        ordering = ["ts_code"]
        verbose_name_plural = "Stock"
        db_table = 'stock'


class StockDetail(models.Model):

    ts_code = models.CharField(max_length=10, blank=True, primary_key=True, verbose_name="股票代码")
    # 日线行情
    trade_date = models.CharField(max_length=20, blank=True, null=True, verbose_name="交易日期")
    open = models.FloatField(blank=True, null=True, verbose_name="开盘价")
    high = models.FloatField(blank=True, null=True, verbose_name="最高价")
    low = models.FloatField(blank=True, null=True, verbose_name="最低价")
    close = models.FloatField(blank=True, null=True, verbose_name="收盘价")

    pre_close = models.FloatField(blank=True, null=True, verbose_name="昨收价")
    change = models.FloatField(blank=True, null=True, verbose_name="涨跌额")
    pct_chg = models.FloatField(blank=True, null=True, verbose_name="涨跌幅")
    vol = models.FloatField(blank=True, null=True, verbose_name="成交量(手)")
    amount = models.FloatField(blank=True, null=True, verbose_name="成交额(千元)")

    # 每日指标
    turnover_rate = models.FloatField(blank=True, null=True, verbose_name="换手率(%)")
    volume_ratio = models.FloatField(blank=True, null=True, verbose_name="量比")
    pe = models.FloatField(blank=True, null=True, verbose_name="市盈率")
    pb = models.FloatField(blank=True, null=True, verbose_name="市净率")
    ps = models.FloatField(blank=True, null=True, verbose_name="市销率")
    dv_ratio = models.FloatField(blank=True, null=True, verbose_name="股息率")
    total_share = models.FloatField(blank=True, null=True, verbose_name="总股本")
    float_share = models.FloatField(blank=True, null=True, verbose_name="流通股本")
    free_share = models.FloatField(blank=True, null=True, verbose_name="自由流通股本")
    total_mv = models.FloatField(blank=True, null=True, verbose_name="总市值")
    circ_mv = models.FloatField(blank=True, null=True, verbose_name="流通市值")

    buy_sm_vol = models.BigIntegerField(blank=True, null=True, verbose_name="小单买入量")
    buy_sm_amount = models.FloatField(blank=True, null=True, verbose_name="小单买入金额")
    sell_sm_vol = models.BigIntegerField(blank=True, null=True, verbose_name="小单卖出量")
    sell_sm_amount = models.FloatField(blank=True, null=True, verbose_name="小单卖出金额")
    buy_md_vol = models.BigIntegerField(blank=True, null=True, verbose_name="中单买入量")
    buy_md_amount = models.FloatField(blank=True, null=True, verbose_name="中单买入金额")
    sell_md_vol = models.BigIntegerField(blank=True, null=True, verbose_name="中单卖出量")
    sell_md_amount = models.FloatField(blank=True, null=True, verbose_name="中单卖出金额")
    buy_lg_vol = models.BigIntegerField(blank=True, null=True, verbose_name="大单买入量")
    buy_lg_amount = models.FloatField(blank=True, null=True, verbose_name="大单买入金额")
    sell_lg_vol = models.BigIntegerField(blank=True, null=True, verbose_name="大单卖出量")
    sell_lg_amount = models.FloatField(blank=True, null=True, verbose_name="大单卖出金额")
    buy_elg_vol = models.BigIntegerField(blank=True, null=True, verbose_name="特大单买入量")
    buy_elg_amount = models.FloatField(blank=True, null=True, verbose_name="特大单买入金额")
    sell_elg_vol = models.BigIntegerField(blank=True, null=True, verbose_name="特大单卖出量")
    sell_elg_amount = models.FloatField(blank=True, null=True, verbose_name="特大单卖出金额")
    net_mf_vol = models.BigIntegerField(blank=True, null=True, verbose_name="净流入量")
    net_mf_amount = models.FloatField(blank=True, null=True, verbose_name="净流入额")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Dayily"
        db_table = "stockdetail"


def getModel(db_table):
    table_name = db_table
    class MyClassMetaclass(models.base.ModelBase):
        def __new__(cls, name, bases, attrs):
            name += db_table
            return models.base.ModelBase.__new__(cls, name, bases, attrs)


    class MyClass(models.Model):
        __metaclass__ = MyClassMetaclass
        id = models.IntegerField(max_length=20,blank=False)
        ts_code = models.CharField(max_length=10, blank=True, primary_key=True, verbose_name="股票代码")
        # 日线行情
        trade_date = models.CharField(max_length=20, blank=True, null=True, verbose_name="交易日期")
        open = models.FloatField(blank=True, null=True, verbose_name="开盘价")
        high = models.FloatField(blank=True, null=True, verbose_name="最高价")
        low = models.FloatField(blank=True, null=True, verbose_name="最低价")
        close = models.FloatField(blank=True, null=True, verbose_name="收盘价")

        pre_close = models.FloatField(blank=True, null=True, verbose_name="昨收价")
        change = models.FloatField(blank=True, null=True, verbose_name="涨跌额")
        pct_chg = models.FloatField(blank=True, null=True, verbose_name="涨跌幅")
        vol = models.FloatField(blank=True, null=True, verbose_name="成交量(手)")
        amount = models.FloatField(blank=True, null=True, verbose_name="成交额(千元)")

        # 每日指标
        turnover_rate = models.FloatField(blank=True, null=True, verbose_name="换手率(%)")
        volume_ratio = models.FloatField(blank=True, null=True, verbose_name="量比")
        pe = models.FloatField(blank=True, null=True, verbose_name="市盈率")
        pb = models.FloatField(blank=True, null=True, verbose_name="市净率")
        ps = models.FloatField(blank=True, null=True, verbose_name="市销率")
        dv_ratio = models.FloatField(blank=True, null=True, verbose_name="股息率")
        total_share = models.FloatField(blank=True, null=True, verbose_name="总股本")
        float_share = models.FloatField(blank=True, null=True, verbose_name="流通股本")
        free_share = models.FloatField(blank=True, null=True, verbose_name="自由流通股本")
        total_mv = models.FloatField(blank=True, null=True, verbose_name="总市值")
        circ_mv = models.FloatField(blank=True, null=True, verbose_name="流通市值")

        buy_sm_vol = models.BigIntegerField(blank=True, null=True, verbose_name="小单买入量")
        buy_sm_amount = models.FloatField(blank=True, null=True, verbose_name="小单买入金额")
        sell_sm_vol = models.BigIntegerField(blank=True, null=True, verbose_name="小单卖出量")
        sell_sm_amount = models.FloatField(blank=True, null=True, verbose_name="小单卖出金额")
        buy_md_vol = models.BigIntegerField(blank=True, null=True, verbose_name="中单买入量")
        buy_md_amount = models.FloatField(blank=True, null=True, verbose_name="中单买入金额")
        sell_md_vol = models.BigIntegerField(blank=True, null=True, verbose_name="中单卖出量")
        sell_md_amount = models.FloatField(blank=True, null=True, verbose_name="中单卖出金额")
        buy_lg_vol = models.BigIntegerField(blank=True, null=True, verbose_name="大单买入量")
        buy_lg_amount = models.FloatField(blank=True, null=True, verbose_name="大单买入金额")
        sell_lg_vol = models.BigIntegerField(blank=True, null=True, verbose_name="大单卖出量")
        sell_lg_amount = models.FloatField(blank=True, null=True, verbose_name="大单卖出金额")
        buy_elg_vol = models.BigIntegerField(blank=True, null=True, verbose_name="特大单买入量")
        buy_elg_amount = models.FloatField(blank=True, null=True, verbose_name="特大单买入金额")
        sell_elg_vol = models.BigIntegerField(blank=True, null=True, verbose_name="特大单卖出量")
        sell_elg_amount = models.FloatField(blank=True, null=True, verbose_name="特大单卖出金额")
        net_mf_vol = models.BigIntegerField(blank=True, null=True, verbose_name="净流入量")
        net_mf_amount = models.FloatField(blank=True, null=True, verbose_name="净流入额")
        class Meta:
            db_table = table_name


    return MyClass
