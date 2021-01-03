import cv2
import numpy as np
from tkinter import messagebox

openPicName="starnight.png"
wndName="picture"
savePicName="theSavePicure.jpg"

# cv2.IMREAD_COLOR：彩色图，默认值(1) - 
# cv2.IMREAD_GRAYSCALE：灰度图(0) - 
# cv2.IMREAD_UNCHANGED：包含透明通道的彩色图(-1)
img=cv2.imread(openPicName,0)
print(img.shape[:2])#打印图像的分辨率
print(img)

# 窗口大小不可以改变:cv2.WINDOW_AUTOSIZE
# 窗口大小可以改变:cv2.WINDOW_NORMAL
# 窗口大小自适应比例：cv2.WINDOW_FREERATIO
# 窗口大小保持比例：cv2.WINDOW_KEEPRATIO
# 显示色彩变成暗色：cv2.WINDOW_GUI_EXPANDED
cv2.namedWindow(wndName, cv2.WINDOW_AUTOSIZE)# 命名窗口名，并设置打开方式
cv2.imshow(wndName,img)#展示图片

kb=cv2.waitKey(0)
if kb==ord('s'):#如果按下了s
    cv2.imwrite(savePicName,img)#将img存为tupian1.jpg
elif kb==ord('q'):
    messagebox.showinfo("提示","我是一个提示框")
elif kb==ord('w'):
    messagebox.showerror("提示","我是一个错误框")
elif kb==ord('e'):
    messagebox.showwarning("提示","我是一个警告框")

cv2.destroyAllWindows()