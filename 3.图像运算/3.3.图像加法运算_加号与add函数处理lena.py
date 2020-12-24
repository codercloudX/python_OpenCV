import cv2 
import numpy as np

wndName1="a"
wndName2="result1"
wndName3="result2"

a=cv2.imread("../lena.jpg",0)
b=a
result1=a+b
result2=cv2.add(a,b)

cv2.namedWindow(wndName1,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName1,a)

cv2.namedWindow(wndName2,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName2,result1)

cv2.namedWindow(wndName3,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName3,result2)


cv2.waitKey(0)

