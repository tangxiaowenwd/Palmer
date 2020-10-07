# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/10/6 21:17
import numpy.fft as nf

#nf(原函数值序列) --》 目标函数序列
#通过一个复数数组 复数的模代表的是振幅，复数的福角代表的初相位，经过逆向傅里叶变换得到合成的函数值数组
"""
    傅里叶定理：
        任何一条周期曲线，无论多么跳跃或不规则,都能表示成一组光滑正玄曲线叠加之和
    傅里叶变换：
    基于傅里叶定理对一条周期曲线进行拆解的过程，最终得到一组光滑的正玄曲线。
    傅里叶变换的目的是可将时域上的信号换变为频域上的信号，随着域的不同，对同一个事物的了解角度也随之改变，因此在时域中
    某些不好处理的地方，在频域就可以较为简单的处理，这就可以大量减少处理信号存储量
"""

import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(0,10000,10000)
print(x)
y1 = 19 * x**4 + 3 * x**3 + 2 * x**2 +np.pi*np.cos(x)
mp.subplot(121)
mp.grid(linestyle=":")
mp.plot(x,y1,label="y1",alpha=0.3)

complex_ary = nf.fft(y1) #复数的数组
#合成波
y_ = nf.ifft(complex_ary).real
mp.plot(x,y_,label="y_",alpha=0.8)

#绘制频域图像， 频率/能量图像
freqs = nf.fftfreq(y_.size,x[1]-x[0])
pows = np.abs(complex_ary)
mp.subplot(122)
mp.grid(linestyle=":")
mp.plot(freqs,pows,color='blue',label="Frquency")
mp.legend()
mp.show()