# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/10/6 21:17
import numpy.fft as nf
import numpy as np
import matplotlib.pyplot as mp
import scipy.io.wavfile as wf




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