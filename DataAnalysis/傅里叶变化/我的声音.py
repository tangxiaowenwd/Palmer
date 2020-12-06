# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/10/7 13:35
import numpy as np
import numpy.fft as nf
import scipy.io.wavfile as wf
import matplotlib.pyplot as mp

filename = "E:\Github\Palmer\DataAnalysis\data\\videos\\aib.wav"
new_filename = filename.split(".")[0]+"new" + ".wav"
#采样率（每秒采样点的个数），采样位移
sample_rate, noised_sigs = wf.read(filename)
noised_sigs = noised_sigs.reshape((368640,)) / (2**15)
times = np.arange(noised_sigs.size) / sample_rate

mp.figure("Filter",facecolor="lightgray")
mp.subplot(221)
mp.title("img1",fontsize=16)
mp.ylabel("Noised Signal")
mp.grid(linestyle=":")
mp.plot(times[7000:8000],noised_sigs[7000:8000],color='dodgerblue',label="noised")


#基于傅里叶变换，获取音频域信息
frqes = nf.fftfreq(times.size,times[1]-times[0])
complex_ary = nf.fft(noised_sigs)
pows = np.abs(complex_ary)  #能量
mp.subplot(222)
mp.title("freqs",fontsize=16)
mp.ylabel("Noised Signal")
mp.grid(linestyle=":")
mp.semilogy(frqes,pows,color='orangered',label="freqs")

#将低能噪声去除后绘制音频频域:频域/能量图像

#找到pow最高音的
fund_fred = np.sort(pows)[-30000]
index = np.argwhere(pows < fund_fred)
index = index.reshape((index.size,))
# for i in index:
#     complex_ary[i] = 0



# noised_index = np.where(frqes != fund_fred)
# #把噪声的位置的复数数据抹掉
# complex_ary[noised_index] = 0

pows = np.abs(complex_ary)
mp.subplot(224)
mp.title("freq",fontsize=16)
mp.ylabel("Noised Signal")
mp.grid(linestyle=":")
mp.plot(frqes,pows,color='orangered',label="freqs")


fitter_sigs = nf.ifft(complex_ary)
mp.subplot(223)
mp.title("img2",fontsize=16)
mp.ylabel("Noised Signal")
mp.grid(linestyle=":")
mp.plot(times[7000:8000],fitter_sigs[7000:8000],color='dodgerblue',label="noised")


wf.write(new_filename,sample_rate,(fitter_sigs*2**15).astype(np.int16))
mp.legend()
mp.tight_layout()
mp.show()