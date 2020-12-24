import cv2
import numpy as np

wndName1="pic1"
wndName2="pic2"
wndName3="pic3"

lena=cv2.imread("../lena.jpg",0)
rows,cols=lena.shape[:2]
src=np.random.randint(0,255,size=[rows,cols],dtype=np.uint8)#没有最后一个参数会报错

dst=cv2.add(src,lena)

cv2.namedWindow(wndName1,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName1,lena)

cv2.namedWindow(wndName2,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName2,src)

cv2.namedWindow(wndName3,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName3,dst)

cv2.waitKey(0)
