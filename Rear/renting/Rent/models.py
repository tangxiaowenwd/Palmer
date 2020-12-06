from django.db import models
# Create your models here.

JobTypes = [
    ("0","技术类"),
    ("1","管理类"),
    ("2","运营类"),
]

Mold = [
    ("0","招室友"),
    ("1","找房子"),
]

class Rent(models.Model):
    """
    title:标题 rent:租金 payment:付款方式 housetype:房型
    addr:位置 size:大小 orientation：朝向 estate:所在小区

    """
    title = models.CharField(max_length=25,blank=False,verbose_name="标题",default="")
    mold = models.CharField(max_length=25,blank=False,verbose_name="类型",choices=Mold,default="")
    addr = models.CharField(max_length=25, blank=False, verbose_name="位置",default="")
    size = models.CharField(max_length=25, blank=False, verbose_name="房间大小",default="")
    orientation = models.CharField(max_length=25, blank=False, verbose_name="朝向",default="")
    estate = models.CharField(max_length=25, blank=False, verbose_name="所在小区",default="")
    rent = models.CharField(max_length=25, blank=False, verbose_name="租金",default="")
    payment = models.CharField(max_length=25, blank=False, verbose_name="付款方式",default="")
    public_facilities = models.CharField(max_length=25, blank=False, verbose_name="公共设施",default="")
    details = models.TextField(max_length=1024,blank=False,verbose_name="房屋描述",default="此人很懒，什么也没有留下------------")

    images = models.ImageField(verbose_name="图片")

    class Meta:
        db_table = "Rent"


    def __unicode__(self):
        return self.title

    # 新加上这个就行了
    def __str__(self):
        return self.title


class User(models.Model):

    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'