import cv2
import numpy as np

wndName1="pic1"

#1.
# src=np.zeros((300,300,3),dtype=np.uint8)
# for i in range(0,300):
    # for j in range(0,300):
        # src[i,j]=(np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255))

#2.
src=np.random.randint(0,256,size=[100,100,3],dtype=np.uint8)

cv2.namedWindow(wndName1,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName1,src)

cv2.waitKey(0)

