import cv2
import numpy as np
import random#生成随机数的模块

wndName1="pic1"
src=cv2.imread("../lena.jpg",1)

#1.
for i in range(10,100):
    for j in range(10,100):
        src[i,j]=random.randint(0,255)#random.randint(0,255),从0-255中随机生成一个整型数
        
#2.
# src[10:100,10:100]=random.randint(0,255)#这样只能产生一种颜色，想要所有颜色都不一样只能用方法1遍历


cv2.namedWindow(wndName1,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName1,src)
cv2.waitKey(0)