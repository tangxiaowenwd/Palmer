# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/10/5 16:38
import numpy as np
import cv2
from time import sleep
cap = cv2.VideoCapture(0) #代表调取摄像头资源，其中0代表电脑摄像头，1代表外接摄像头(usb摄像头)
width = 640
height = 480
w = 360
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

while(True):
    cap = cv2.VideoCapture(0)  # 代表调取摄像头资源，其中0代表电脑摄像头，1代表外接摄像头(usb摄像头)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    ret,frame=cap.read()
    #灰度化
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    cap.release()
    cv2.destroyAllWindows() #释放窗口
    cv2.imwrite('filepahe.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY),100])