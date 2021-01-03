import cv2 
import numpy as np

wndName1="pic1"
wndName2="pic2"
wndName3="pic3"

src1=np.zeros((5,5),dtype=np.uint8)
src2=np.random.randint(0,256,(5,5),dtype=np.uint8)
src2[0:3,0:3]=255
src2[4,4]=255
result=cv2.bitwise_and(src1,src2)

cv2.namedWindow(wndName1,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName1,src1)

cv2.namedWindow(wndName2,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName2,src1)

cv2.namedWindow(wndName3,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName3,result)

cv2.waitKey(0)

