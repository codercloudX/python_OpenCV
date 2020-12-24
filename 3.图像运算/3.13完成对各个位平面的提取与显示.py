import cv2 
import numpy as np



lena=cv2.imread("../lena.jpg",0)
cv2.imshow("lena",lena)
rows,cols=lena.shape

#1.构造用于提取位平面的提取矩阵
#将像素值为1,2,4,8,16,32,128的图像取出来放在一个数组里
x=np.zeros((rows,cols,8),dtype=np.uint8)
for i in range(8):
    x[:,:,i]=2**i 
#此时：
#x[:,:,1]==2,  x[:,:,2]==4,x[:,:,3]==8,x[:,:,4]==16,
#x[:,:,5]==32,  x[:,:,6]==64,x[:,:,7]==128,x[:,:,0]==1

#2.将提取的图像与原图像做按位与运算，得出位平面图
r=np.zeros((rows,cols,8),dtype=np.uint8)
for i in range(8):
    r[:,:,i]=cv2.bitwise_and(lena,x[:,:,i])
    mask=r[:,:,i]>0#将得到的位平面进行阈值处理，将其中的8调整为255
    cv2.imshow(str(i),r[:,:,i])

cv2.waitKey(0)

