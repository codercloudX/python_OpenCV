import cv2 
import numpy as np

wndName1="pic1"
wndName2="pic2"
wndName3="pic3"

lena=cv2.imread("../lena.jpg",1)
rows,cols=lena.shape[:2]
# newImg=np.random.randint(0,1,(rows,cols),dtype=np.uint8)#这一句，newImg的值是灰度图，无法和彩色图像lena进行按位与运算。
newImg=np.zeros(lena.shape,dtype=np.uint8)#这一句，newImg的值是二值图，可以和彩色图像lena进行按位与运算。
newImg[100:400,200:400]=255
newImg[100:500,100:200]=255
result=cv2.bitwise_and(lena,newImg)

gamma=0


cv2.namedWindow(wndName1,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName1,lena)

cv2.namedWindow(wndName2,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName2,newImg)

cv2.namedWindow(wndName3,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName3,result)


cv2.waitKey(0)

