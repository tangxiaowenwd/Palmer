# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/10/6 20:59
import numpy as np


"""
    有一个矩阵，可以分解为3个矩阵 U S V ，使得 U x S x V等于M.U与V都是正交矩阵（乘以自身的转置矩阵结果为单位矩阵），
    那么S矩阵主对角线的元素称为M的奇异值，其他元素为零
"""

# M = np.mat('4 11 14;8 7 -2')
# U,sv,V = np.linalg.svd(M,full_matrices=False)
# print(U)
# print(sv)
# print(V)
# print(U*U.T)
# print(np.diag(sv))
# print(V*V.T)
#
# print(U*np.diag(sv)*V)

import cv2
import matplotlib.pyplot as mp


img_rgb= cv2.imread("E:\Github\Palmer\DataAnalysis\data\\flow.jpg",cv2.IMREAD_GRAYSCALE)
# b,g,r = cv2.split(img)
# img_rgb = cv2.merge([r,g,b])
mp.subplot(221)
cropped = np.mat(img_rgb)
mp.imshow(cropped)
U,sv,V = np.linalg.svd(cropped,full_matrices=False)

dst = U*np.diag(sv)*V
mp.subplot(222)
mp.imshow(dst.real)

mp.subplot(223)
sv[200:] = 0
dst = U*np.diag(sv)*V
mp.imshow(dst.real)

mp.subplot(224)
sv[20:] = 0
dst = U*np.diag(sv)*V
mp.imshow(dst.real)
mp.show()

