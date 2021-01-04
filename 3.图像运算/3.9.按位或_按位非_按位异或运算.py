import cv2 
import numpy as np

wndName1="pic1"
wndName2="pic2"
wndName3="pic3"

lena=cv2.imread("../lena.jpg",1)
rows,cols=lena.shape[:2]

newImg=np.zeros(lena.shape,dtype=np.uint8)
newImg[100:400,200:400]=255
newImg[100:500,100:200]=255
# result=cv2.bitwise_or(lena,newImg)#按位或
result=cv2.bitwise_not(newImg)#按位非
# result=cv2.bitwise_xor(lena,newImg)#按位异或


cv2.namedWindow(wndName1,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName1,lena)

cv2.namedWindow(wndName2,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName2,newImg)

cv2.namedWindow(wndName3,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName3,result)


cv2.waitKey(0)

