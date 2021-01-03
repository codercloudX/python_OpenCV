import cv2
import numpy as np

img=np.random.randint(0,256,size=[200,400],dtype=np.uint8)
dst=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
print(img[1,1])
print(dst[1,1])
#当灰度图转换成BGR图时，该位置的像素值会变成该位置三个通道的像素值

cv2.imshow("img",img)
cv2.imshow("dst",dst)

cv2.waitKey(0)
