# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/10/19 20:53
from django.conf.urls import url
from Rent import views

urlpatterns = [
    url(r"^index/",views.index,name='index')
]


urlpatterns += [
    url(r"^login/",views.login,name='login'),
    url(r"^register/",views.register,name='register'),
    url(r'^logout/', views.logout),
]

urlpatterns += [
    url(r"^image/",views.image,name='image'),
]