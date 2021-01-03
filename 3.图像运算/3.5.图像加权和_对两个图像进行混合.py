import cv2 
import numpy as np

wndName1="pic1"
wndName2="pic2"
wndName3="pic3"

lena=cv2.imread("../lena.jpg",0)
dmbz=cv2.imread("../dmbz.jpg",0)
rows,cols=lena.shape[:2]
dmbzROI=dmbz[0:rows,0:cols]
gamma=0

#加权和运算：
#src*alpha+src2*beta+gamma
#alpha是src1的系数，beta是src2的系数，gamma是亮度调节值
dst=cv2.addWeighted(lena,0.5,dmbzROI,0.5,gamma)#两个系数之和，最好等于1

cv2.namedWindow(wndName1,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName1,lena)

cv2.namedWindow(wndName2,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName2,dmbzROI)

cv2.namedWindow(wndName3,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName3,dst)

cv2.waitKey(0)

