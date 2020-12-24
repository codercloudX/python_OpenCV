import cv2
import numpy as np
import random#生成随机数的模块

wndName1="pic1"
src=cv2.imread("../lena.jpg",1)

for i in range(10,100):
    for j in range(10,100):
        src[i,j]=random.randint(0,255)#random.randint(0,255),从0-255中随机生成一个整型数


cv2.namedWindow(wndName1,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName1,src)
cv2.waitKey(0)