import cv2 
import numpy as np

wndName1="pic1"
wndName2="pic2"
wndName3="pic3"

lena=cv2.imread("../lena.jpg",0)
rows,cols=lena.shape[:2]

newImg=np.zeros(lena.shape,dtype=np.uint8)
<<<<<<< HEAD
newImg[:rows,:cols]=127#这里第i个位平面对应的像素值。比如第3个位平面就是2的3次方-1，这里是127，就是2的7次方-1，即第7个位平面对应的像素值
=======
newImg[:rows,:cols]=0#这里第i个位平面对应的像素值。比如第3个位平面就是2的3次方-1，这里是127，就是2的7次方-1，即第7个位平面对应的像素值
>>>>>>> afb766743f3840539a4307408386a48a1833c9c2
result=cv2.bitwise_and(lena,newImg)#对原图像与提取矩阵做按位与运算，得出位平面分解后的图像，即称位平面

print(result)
cv2.namedWindow(wndName1,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName1,lena)

cv2.namedWindow(wndName2,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName2,newImg)

cv2.namedWindow(wndName3,cv2.WINDOW_AUTOSIZE)
cv2.imshow(wndName3,result)


cv2.waitKey(0)

