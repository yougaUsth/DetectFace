#-*- coding:utf-8 -*-
import cv2
import numpy
from PIL import Image, ImageDraw
import os
"""
    cv2.IMREAD_COLOR 读入彩色图像
    cv2.IMREAD_GRAYSCALE 以灰度模式读入图像
"""
print cv2.__version__


def detect_face(image_name):
    OPEN_CV_PATH = r"E:\SOFT\opencv3.2\opencv\build\etc\haarcascades"
    img = cv2.imread(image_name, cv2.IMREAD_COLOR)
    face_cascade = cv2.CascadeClassifier(OPEN_CV_PATH+"\haarcascade_frontalface_alt2.xml")

    # if语句：如果img维度为3，说明不是灰度图，先转化为灰度图gray，如果不为3，也就是2，原图就是灰度图
    if img.ndim == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img

    #1.3和5是特征的最小、最大检测窗口，它改变检测结果也会改变
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    result = []
    for (x,y,width,height) in faces:
        result.append((x,y,x+width,y+height))
    return result

def save_faces(image_name):
    faces = detect_face(image_name)
    if faces:
        #将人脸保存在save_dir目录下。
        #Image模块：Image.open获取图像句柄，crop剪切图像(剪切的区域就是detectFaces返回的坐标)，save保存。
        save_dir = image_name.split('.')[0]+"_faces"
        if not os.path.exists(save_dir) :
            os.mkdir(save_dir)
        count = 0
        for (x1,y1,x2,y2) in faces:
            file_name = os.path.join(save_dir,str(count)+".jpg")
            Image.open(image_name).crop((x1,y1,x2,y2)).save(file_name)
            count+=1

def draw_faces(image_name):
    faces = detect_face(image_name)
    if faces:
        img = Image.open(image_name)
        draw_instance = ImageDraw.Draw(img)
        for (x1,y1,x2,y2) in faces:
            draw_instance.rectangle((x1,y1,x2,y2), outline=(255, 0,0))
        img.save('drawfaces_'+image_name)


if __name__ == '__main__':
    draw_faces("002.png")