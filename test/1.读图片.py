import cv2
import numpy as np
openPicName="starnight.png"
wndName="picture"
savePicName="theSavePicure.jpg"

# cv2.IMREAD_COLOR：彩色图，默认值(1) - 
# cv2.IMREAD_GRAYSCALE：灰度图(0) - 
# cv2.IMREAD_UNCHANGED：包含透明通道的彩色图(-1)
img=cv2.imread(openPicName,0)
dst=cv2.resize(img,(800,600),interpolation=cv2.INTER_NEAREST)
print(dst.shape[:2])
cv2.namedWindow(wndName, cv2.WINDOW_AUTOSIZE)# 命名窗口名，并设置打开方式
cv2.imshow(wndName,dst)#展示图片

kb=cv2.waitKey(0)
if kb==ord('s'):#如果按下了s
    cv2.imwrite(savePicName,dst)#将img存为tupian1.jpg

cv2.destroyAllWindows()