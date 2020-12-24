import cv2
import numpy as np

wndName1="pic1"

src=cv2.imread("feiji.jpg")
dst=cv2.resize(src,(300,300),interpolation=cv2.INTER_NEAREST)

cv2.namedWindow(wndName1,cv2.WINDOW_NORMAL)
cv2.imshow(wndName1,dst)

cv2.waitKey(0)