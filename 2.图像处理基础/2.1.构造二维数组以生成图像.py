import cv2
import numpy as np


wndName1="pic1"

i,j=0,0
src =np.zeros((30,30),dtype=np.uint8)#生成一个8*8的二维数组
rows,cols=src.shape[:2]

#将10行-100行，80列-100列的元素变成白色
#1.
# for i in range(0,30):
    # for j in range(10,20):
        # src[i,j]=127
        
#2.
src[0:30,10:20]=127
        
#输出每个像素对应的元素坐标
for i in range(rows):
    for j in range(cols):
        print("[%d %d]" % (i,j),end="\t")

cv2.namedWindow(wndName1,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName1,src)

cv2.waitKey(0)