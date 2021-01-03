import cv2
import numpy as np

wndName1="pic1"
wndName2="pic2"
wndName3="pic3"

src1=np.random.randint(0,255,(3,3,3),dtype=np.uint8)
src2=np.random.randint(0,255,(3,3,3),dtype=np.uint8)
src3=src1+src2
print("src1:",src1)
print()
print("src2:",src2)
print()
print("src3:",src3)

cv2.namedWindow(wndName1,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName1,src1)

cv2.namedWindow(wndName2,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName2,src2)

cv2.namedWindow(wndName3,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName3,src3)


cv2.waitKey(0)

