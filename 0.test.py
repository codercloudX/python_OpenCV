import cv2
import numpy as np
openPicName="starnight.png"
wndName1="picture1"
wndName2="picture2"
savePicName="theSavePicure.jpg"



# cv2.IMREAD_COLOR：彩色图，默认值(1) - 
# cv2.IMREAD_GRAYSCALE：灰度图(0) - 
# cv2.IMREAD_UNCHANGED：包含透明通道的彩色图(-1)
img=cv2.imread(openPicName,1)#彩色图
logo=cv2.imread("logo09.jpg",1)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转灰度图
cv2.add(img,logo)


#参数：1.src灰度图，2.thresh阈值，3.maxval最大值，4.type阈值类型
# ret,mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)# 阈值越大，越多像素转成黑色(0)，越少像素转成白色(255),所以白色越少黑色越多
# mask_inv = cv2.bitwise_not(mask)# 对mask进行黑白取反

# cv2.namedWindow(wndName1, cv2.WINDOW_NORMAL)# 命名窗口名，并设置打开方式
# cv2.imshow(wndName1,mask_inv)#展示图片

# cv2.namedWindow(wndName2, cv2.WINDOW_NORMAL)# 命名窗口名，并设置打开方式
# cv2.imshow(wndName2,mask_inv)#展示图片

kb=cv2.waitKey(0)
if kb==ord('s'):#如果按下了s
    cv2.imwrite(savePicName,img)#将img存为tupian1.jpg

cv2.destroyAllWindows()