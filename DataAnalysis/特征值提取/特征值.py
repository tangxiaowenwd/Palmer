# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/10/6 19:23
import numpy as np
import scipy.misc as sm
import cv2


#特征值和特征向量
#特征值必须为方阵
def get_eigvals():
    """
        已知n阶方阵，求特征值和特征向量
        eigvals:特征值数组
        eigvecs:特征向量数组
    """
    A = np.arange(9).reshape(3,3)
    eigvals,eigvecs = np.linalg.eig(A)
    print(eigvals,eigvecs)
    #已知特征值和特征向量求方阵
    s = eigvals * np.diag(eigvecs) * eigvecs


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
