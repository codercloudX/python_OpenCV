import cv2
import numpy as np

#============预处理============#
lena=cv2.imread("../lena.jpg",0)
waterMark=cv2.imread("../watermark1.jpg",0)
#将像素值大于255的像素都置为1
# ret,waterMark=cv2.threshold(waterMark,0,1,cv2.THRESH_BINARY)
w=waterMark[:,:]>0
waterMark[w]=1
rows,cols=lena.shape[:2]
#============嵌入过程==========#
t254=np.ones((rows,cols),dtype=np.uint8)*254#生成元素值都为254的数组
lenaH7=cv2.bitwise_and(lena,t254)#lena与t254进行与运算，获得lena的高七位
e=cv2.bitwise_or(lenaH7,waterMark)#lenaH7与wateMark进行或运算，将waterMark嵌入lenaH7
#============提取过程==========#
t1=np.ones((rows,cols),dtype=np.uint8)#生成元素值都为1的数组
wm=cv2.bitwise_and(e,t1)
#将像素值大于0的像素都置为255
# ret,wm=cv2.threshold(wm,0,255,cv2.THRESH_BINARY)
w=wm[:,:]>0
wm[w]=255
#============显示==============#
cv2.imshow("lena",lena)
cv2.imshow("waterMark",waterMark*255)
cv2.imshow("e",e)
cv2.imshow("wm",wm)

cv2.waitKey(0)
