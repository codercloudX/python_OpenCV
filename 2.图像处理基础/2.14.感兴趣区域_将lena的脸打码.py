import cv2
import numpy as np

wndName1="pic1"
wndName2="face"

src=cv2.imread("../lena.jpg",cv2.IMREAD_UNCHANGED)

face=np.random.randint(0,256,(180,100,3),dtype=np.uint8)#????为什么这里只能填(180,80,3)而不是(180,100,3)
src[220:400,250:350]=face

cv2.namedWindow(wndName2,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName2,face)
cv2.namedWindow(wndName1,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName1,src)

cv2.waitKey(0)

