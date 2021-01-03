import cv2 
import numpy as np

wndName1="pic1"
wndName2="pic2"
wndName3="pic3"

lena=cv2.imread("../lena.jpg",1)
rows,cols=lena.shape[:2]

newImg=np.zeros(lena.shape,dtype=np.uint8)
newImg[:rows,:cols]=np.random.randint(250,255)

result=cv2.add(lena,newImg)#add函数增加亮度，如果只是单纯相加，会导致像素溢出


cv2.namedWindow(wndName1,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName1,lena)

cv2.namedWindow(wndName2,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName2,newImg)

cv2.namedWindow(wndName3,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName3,result)


cv2.waitKey(0)

