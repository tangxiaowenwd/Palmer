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
print(noised_sigs)

times = np.arange(noised_sigs.size) / sample_rate
#基于傅里叶变换，获取音频域信息
frqes = nf.fftfreq(times.size,times[1]-times[0])
complex_ary = nf.fft(noised_sigs)
print(complex_ary)
pows = np.abs(complex_ary)  #能量
print(pows)
fitter_sigs = nf.ifft(complex_ary).real

wf.write(new_filename,sample_rate,fitter_sigs)
