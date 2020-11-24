# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/10/7 11:51
import numpy as np
import numpy.fft as nf
import scipy.io.wavfile as wf
import matplotlib.pyplot as mp

filename = "E:\Github\Palmer\DataAnalysis\data\\videos\\signal.wav"
new_filename = filename.split(".")[0]+"new" + ".wav"
#采样率（每秒采样点的个数），采样位移
sample_rate, noised_sigs = wf.read(filename)


filename1 = "E:\Github\Palmer\DataAnalysis\data\\videos\\noised_new.wav"
new_filename1 = filename.split(".")[0]+"new" + ".wav"
#采样率（每秒采样点的个数），采样位移
sample_rate1, noised_sigs1 = wf.read(filename)


noised_sigs = noised_sigs / (2**15) #把图像控制到1和-1之间
#绘制音频时域的：时间/位移图像

times = np.arange(noised_sigs.size) / sample_rate


mp.figure("Filter",facecolor="lightgray")
# mp.subplot(221)
# mp.title("Time Domain",fontsize=16)
# mp.ylabel("Noised Signal")
# mp.grid(linestyle=":")
# mp.plot(times,noised_sigs,color='dodgerblue',label="noised")

#mp.subplot(221)
mp.title("Time Domain",fontsize=16)
mp.ylabel("Noised Signal")
mp.grid(linestyle=":")
print(times)
print(noised_sigs)
mp.plot(times[:100],noised_sigs[:100],color='dodgerblue',label="noised")
mp.show()

#基于傅里叶变换，获取音频域信息
frqes = nf.fftfreq(times.size,times[1]-times[0])
complex_ary = nf.fft(noised_sigs)
pows = np.abs(complex_ary)  #能量

mp.subplot(222)
mp.title("freqs",fontsize=16)
mp.ylabel("Noised Signal")
mp.grid(linestyle=":")
mp.semilogy(frqes[frqes > 0],pows[frqes > 0],color='orangered',label="freqs")


#将低能噪声去除后绘制音频频域:频域/能量图像
fund_fred = frqes[pows.argmax()]
print(fund_fred)
noised_index = np.where(frqes != fund_fred)
#把噪声的位置的复数数据抹掉
complex_ary[noised_index] = 0
pows = np.abs(complex_ary)
mp.subplot(224)
mp.title("index",fontsize=16)
mp.ylabel("Noised Signal")
mp.grid(linestyle=":")
mp.plot(frqes[frqes > 0],pows[frqes > 0],color='orangered',label="freqs")


#针对滤波过后的复数数组，做逆向傅里叶变换
#绘制时域图像：时间/位移图像
fitter_sigs = nf.ifft(complex_ary)
mp.subplot(223)
mp.title("videx",fontsize=16)
mp.ylabel("Noised Signal")
mp.grid(linestyle=":")
mp.plot(times[:100],fitter_sigs[:100],color='dodgerblue',label="noised")


wf.write(new_filename,sample_rate,(fitter_sigs*2**15).astype(np.int16))
# #合成一个图像
# compound  = "E:\Github\Palmer\DataAnalysis\data\\videos\\hecheng.wav"
# wf.write(compound,sample_rate,noised_sigs1)
# print(compound)
# print(sample_rate)

mp.legend()
mp.tight_layout()
mp.show()

