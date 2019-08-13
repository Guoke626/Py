# encoding=utf-8

import cv2

img = cv2.imread('D:\e42ecb3e64e9dc584c15ad8518c6c4c.png',1)#读取一张图片

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#将图片转化成灰度

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
face_cascade.load('D:\BaiduNetdiskDownload\haarcascade_frontalface_alt2.xml')#一定要告诉编译器文件所在的具体位置
'''此文件是opencv的haar人脸特征分类器'''
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow('img',img)
cv2.waitKey()
