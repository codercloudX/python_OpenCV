import cv2
import numpy as np

wndName1="pic1"

src=np.zeros((300,300,3),dtype=np.uint8)#构造三维数组，[行,列,通道值]
src[:,0:100,0]=255#0是蓝色通道值，此时所有行的0-100列，的RGB值都为(255,0,0),如果将255改为0，则变成黑色
src[:,100:200,1]=255#1是绿色通道值，此时所有行的100-200列，的RGB值都为(0,255,0),如果将255改为0，则变成黑色
src[:,200:300,2]=28#2是红色通道值，此时所有行的200-300列，的RGB值都为(0,0,255),如果将255改为0，则变成黑色
print(src)

cv2.namedWindow(wndName1,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName1,src)

cv2.waitKey(0)
cv2.destroyAllWindows()