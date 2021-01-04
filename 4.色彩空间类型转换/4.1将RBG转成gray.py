import cv2
import numpy as np

img=np.random.randint(0,256,size=[200,400,3],dtype=np.uint8)
dst=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img[1,1][0])
print(img[1,1][1])
print(img[1,1][2])
# Gray=0.299*R+0.587*G+0.114*B
print(dst[1,1])

cv2.imshow("img",img)
cv2.imshow("dst",dst)

cv2.waitKey(0)
