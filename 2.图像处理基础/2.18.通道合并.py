import cv2
import numpy as np

wndName1="lena"
wndName2="rgb"
wndName3="bgr"
wndName4="grb"

lena=cv2.imread("../lena.jpg",cv2.IMREAD_UNCHANGED)
b,g,r=cv2.split(lena)
print(b)
rgb=cv2.merge([r,g,b])
bgr=cv2.merge([b,g,r])
grb=cv2.merge([g,r,b])



cv2.namedWindow(wndName1,cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(wndName2,cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(wndName3,cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(wndName4,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName1,lena)
cv2.imshow(wndName2,rgb)
cv2.imshow(wndName3,bgr)
cv2.imshow(wndName4,grb)

cv2.waitKey(0)

