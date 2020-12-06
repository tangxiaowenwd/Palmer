# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/9/30 23:24
import sys
def func():
    print("niaho")

fun = getattr(sys.modules[__name__], "func")

exec(func)