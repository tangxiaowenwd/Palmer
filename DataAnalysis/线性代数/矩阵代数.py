# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/10/6 20:59
import numpy as np
import cv2
import matplotlib.pyplot as mp


#img_rgb= cv2.imread("E:\Github\Palmer\DataAnalysis\data\\flow.jpg",cv2.IMREAD_GRAYSCALE)
img_rgb= cv2.imread("ren.jpg")
b,g,r = cv2.split(img_rgb)
img_rgb = cv2.merge([r,g,b])



#img_rgb = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY) #彩色图转灰度图

mp.imshow(img_rgb)
mp.show()

