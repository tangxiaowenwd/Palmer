# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/10/5 17:05
# !/usr/bin/python3
import cv2
import time
from datetime import datetime

movie_time = 3000000
def video(cnt):
    file = './video/output' + str(cnt) + ".mp4"
    ## opening videocapture
    cap = cv2.VideoCapture(0)
    ## some videowriter props
    sz = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
          int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fps = 30
    # 定义视频编码器为XVID
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    ## open and set props
    vout = cv2.VideoWriter()
    vout.open(file, fourcc, fps, sz, True)
    a = time.time()
    while True:
        _, frame = cap.read()
        cv2.putText(frame, str(cnt), (10, 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1, cv2.LINE_AA)
        vout.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):  # 按下q后退出条件成立
            break
        if time.time() - a > movie_time:
            #print("结束时间",datetime.now().strftime("%Y-%m-%d, %H:%M:%S"))
            break
    # 释放内存
    cap.release()
    cv2.destroyAllWindows()

cnt = 0
a = time.time()
video(cnt)
while True:
    video(cnt)
    cnt += 1

