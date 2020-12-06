# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/9/6 15:40
import os
import shutil

start_file = "E:\BaiduNetdiskDownload\网页模板"
end_file = "E:\BaiduNetdiskDownload\images"

img = [".jpg",'.png']

def get_dir(file_dir):
    #遍历文件夹,找到图片
    try:
        files = os.listdir(file_dir)
        #判断是不是文件夹
        for file in files:
            new_file = file_dir+"\\"+file
            if os.path.isdir(new_file):
                get_dir(new_file)
            elif os.path.isfile(new_file):
                if os.path.splitext(new_file)[1] in img:
                    move_file(new_file,os.path.splitext(new_file)[1])
    except Exception as e:
        pass
n = 0
def move_file(file,expand):
    global n
    dst = end_file + "\\" + str(n) + expand
    shutil.move(file, dst)
    n += 1


if __name__=="__main__":
    get_dir(start_file)



