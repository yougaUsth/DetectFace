#-*- coding:utf-8 -*-
import cv2


def threshold():
    #读入灰度图
    img = cv2.imread("002.png",cv2.IMREAD_GRAYSCALE)
    ret,th = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    cv2.imshow('thresh', th)
    cv2.waitKey(0)

if __name__ == '__main__':
    threshold()