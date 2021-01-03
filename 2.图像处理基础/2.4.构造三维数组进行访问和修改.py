import cv2
import numpy as np


wndName1="pic1"

i,j=0,0
src =np.zeros((100,100,3),dtype=np.uint8)#生成一个30*30*3的三维数组，表示30行30列3个通道
rows,cols=src.shape[:2]

# src[15,15]=[255,0,0]#第一个值是蓝色通道
# src[20,20]=[0,255,0]#第二个值是绿色通道
# src[25,25]=[0,0,255]#第三个值是红色通道

for i in range(rows):
    for j in range(cols):
        if i==j:
            src[i,j]=[127,127,127]
            
# print(src)


cv2.namedWindow(wndName1,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName1,src)

cv2.waitKey(0)