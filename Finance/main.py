# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/9/30 22:26
from BasicInfo.BasicInfo import GetInfo
from Graphic.Graphic import Grasphic




name,data = GetInfo("600520.SH").main()
Grasphic(data,name,["K"])


