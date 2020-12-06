# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/10/7 19:15
import scipy.integrate as sci
import numpy as np
from matplotlib.patches import Polygon
from matplotlib.pyplot import mp

a = 0.5
b = 9.5
x = np.linspace(0,10)
print(x)

fig,ax = mp.subplots(figsize=(7,5))