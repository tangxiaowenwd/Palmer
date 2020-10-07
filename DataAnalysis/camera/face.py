# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/10/5 21:57
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
    color = (255, 255, 0)
    while True:
        _, frame = cap.read()
        classifier = cv2.CascadeClassifier("E:\Github\Palmer\DataAnalysis\data\haarcascade_frontalface_default.xml")
        faceRects = classifier.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5, minSize=(32, 32))
        if len(faceRects):  # 大于0则检测到人脸
            for faceRect in faceRects:  # 单独框出每一张人脸
                x, y, w, h = faceRect
                print(frame.shape)
                print(x,y,w,h)
                # 框出人脸
                cv2.circle(frame, (x+w//2,y+h//2), min(w // 2, h // 2), (255, 25, 0))
                # 左眼
                cv2.circle(frame, (x + w // 4 +15, y + h // 4 + 30), min(w // 8, h // 8), color)
                # 右眼
                cv2.circle(frame, (x + 3 * w // 4 -15, y + h // 4 + 30), min(w // 8, h // 8), color)
                # 嘴巴
                cv2.circle(frame, (x+w//2,y+h//2 + 60), min(x//8, y//8), color)
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

