import cv2
import numpy as np

wndName1="b通道"
wndName2="g通道"
wndName3="r通道"

lena=cv2.imread("../lena.jpg",cv2.IMREAD_UNCHANGED)
b=lena[:,:,0]
g=lena[:,:,1]
r=lena[:,:,2]



cv2.namedWindow(wndName1,cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(wndName2,cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(wndName3,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName1,b)
cv2.imshow(wndName2,g)
cv2.imshow(wndName3,r)

cv2.waitKey(0)

