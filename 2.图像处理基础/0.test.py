import cv2
import numpy as np

lena=cv2.imread("../lena.jpg",1)[100:200,300:400]
lenaB=lena[:,:,0]
lenaG=lena[:,:,1]
lenaR=lena[:,:,2]

cv2.imshow("lena",lena)
cv2.imshow("lenaB",lenaB)
cv2.imshow("lenaG",lenaG)
cv2.imshow("lenaR",lenaR)

cv2.waitKey(0)