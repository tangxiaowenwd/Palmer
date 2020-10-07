# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/10/6 19:32
import scipy.misc as sm
import numpy as np
import cv2
import matplotlib.pyplot as mp


img_rgb= cv2.imread("E:\Github\Palmer\DataAnalysis\data\\flow.jpg",cv2.IMREAD_GRAYSCALE)
# b,g,r = cv2.split(img)
# img_rgb = cv2.merge([r,g,b])

cropped = img_rgb[0:375, 95:470]
cropped = np.mat(cropped)
mp.imshow(cropped)
mp.show()
eigvals,eigvecs = np.linalg.eig(cropped)
#eigvals[200:] = 0
eigvecs[200:0] = 0
dst = eigvecs * np.diag(eigvals) * eigvecs.I
mp.imshow(dst.real)
mp.show()


