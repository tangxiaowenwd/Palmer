# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/10/6 22:15
import cv2
import matplotlib.pyplot as mp
import numpy as np
import time
from moviepy.editor import VideoFileClip
import sys

def get_file_times(filename):
    u"""
    获取视频时长（s:秒）
    """
    clip = VideoFileClip(filename)
    print(clip.duration)
    #file_time = timeConvert(clip.duration)
    return clip.duration

def timeConvert(size):  # 单位换算
    print(size)
    M, H = 60, 60 ** 2
    if size < M:
        return str(size) + u'秒'
    if size < H:
        return u'%s分钟%s秒' % (int(size / M), int(size % M))
    else:
        hour = int(size / H)
        mine = int(size % H / M)
        second = int(size % H % M)
        tim_srt = u'%s小时%s分钟%s秒' % (hour, mine, second)
        return tim_srt

def getFrame(videoPath, svPath):
    size = get_file_times(videoPath)
    size = int(float(size)) + 1
    cap = cv2.VideoCapture(videoPath)
    numFrame = 23 #24张照片保存一张
    cnt = 0
    endtime = time.time() + size+600
    while time.time() < endtime:
        if cap.grab():
            flag, frame = cap.retrieve()
            if not flag:
                continue
            else:
                cv2.imshow('video', frame)
                numFrame += 1
                if numFrame % 24 == 0:
                    cnt += 1
                    newPath = svPath + str(cnt) + ".jpg"
                    mp.imshow(frame)
                    mp.savefig(newPath)
                    mp.clf()
                    #cv2.imencode('.jpg', frame)[1].tofile(newPath)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if numFrame == 200:
            break
    # 释放内存
    cap.release()
    cv2.destroyAllWindows()

videoPath = "E:\Github\Palmer\DataAnalysis\data\\a.mp4"
savePicturePath = "E:\Github\Palmer\DataAnalysis\camera\image\image"

getFrame(videoPath, savePicturePath)