import cv2
import numpy as np

lena=cv2.imread("../lena.jpg",1)[100:200,300:400]
src=np.zeros((30,30,3),dtype=np.uint8)
for i in range(0,30):
    for j in range(10,20):
        src[i,j,0]=0
        src[i,j,1]=255
        src[i,j,2]=255

cv2.imshow("src",src)

cv2.waitKey(0)