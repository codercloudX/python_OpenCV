import cv2
import numpy as np
wndName="摄像头"

capture=cv2.VideoCapture(0)
while(True):
    ret,frame=capture.read()# 获取一帧
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)# 将这帧转成灰度图
    cv2.namedWindow(wndName,cv2.WINDOW_NORMAL)# 命名窗口名
    cv2.imshow(wndName,gray)# 展示窗口
    if cv2.waitKey(0)==ord('q'):
        break