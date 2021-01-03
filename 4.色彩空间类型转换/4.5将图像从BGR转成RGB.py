import cv2
import numpy as np

src=cv2.imread("../lena.jpg",1)
gray=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
rgb=cv2.cvtColor(src,cv2.COLOR_BGR2RGB)

cv2.imshow("src",src)
cv2.imshow("gray",gray)
cv2.imshow("rgb",rgb)

cv2.waitKey(0)