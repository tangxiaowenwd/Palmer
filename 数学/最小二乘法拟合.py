# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/10/7 19:23
# encoding: utf8

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from sklearn.linear_model import LinearRegression
from scipy import sparse

matplotlib.matplotlib_fname()  # 将会获得matplotlib包所在文件夹
font = FontProperties()
plt.rcParams['font.sans-serif'] = ['Droid Sans Fallback']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

plt.figure()

plt.title(u' 可爱女生的数据 ')

plt.xlabel(u'x 体重')

plt.ylabel(u'y 身高')

plt.axis([40, 80, 140, 200])

plt.grid(True)

x = [[48], [57], [50], [54], [64], [61], [43], [59]]

y = [[165], [165], [157], [170], [175], [165], [155], [170]]

plt.plot(x, y, 'k.')

model = LinearRegression()

model.fit(x, y)

plt.show()
