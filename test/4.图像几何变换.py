import cv2
import numpy as np

wndName_1="src"
wndName_2="dst"

src=cv2.imread("dmbz.jpg",1)
rows, cols = src.shape[:2]
#1.缩放
# INTER_NEAREST	最近邻插值
# INTER_LINEAR	双线性插值（默认设置）
# INTER_AREA	使用像素区域关系进行重采样。 它可能是图像抽取的首选方法，因为它会产生无云纹理的结果。 但是当图像缩放时，它类似于INTER_NEAREST方法。
# INTER_CUBIC	4x4像素邻域的双三次插值
# INTER_LANCZOS4	8x8像素邻域的Lanczos插值
dst=cv2.resize(src,(200,150),interpolation=cv2.INTER_NEAREST)#第二个参数是分辨率，第三个参数是缩放方式

#2.翻转
# 参数2 = 0：垂直翻转(沿x轴)，
# 参数2 > 0: 水平翻转(沿y轴)，
# 参数2 < 0: 水平垂直翻转
# dst=cv2.flip(dst,1)


#3.平移
# 如果需要沿 $(x,y)$方向移动，移动的距离是$(t_x,t_y)$,需要构建移动矩阵
# 你可以使用 Numpy 数组构建这个矩阵，数据类型是 np.float32，然后把它传给函数 cv2.warpAffine()
# opencv2和opencv3中对图像的旋转和平移都是通过仿射变换函数cv::warpAffine()来实现的
M = np.float32([[1, 0, 50], [0, 1, 50]])#固定格式：[[1, 0, 横向偏移量], [0, 1, 纵向偏移量]，np.float32()可以将二元数组转化成浮点数
dst = cv2.warpAffine(src, M, (rows, cols))  #这个方法返回经过仿射变换计算后的图像,warpAffine(原图像，仿射变换矩阵，(宽,高))

#4.旋转
# cv2.getRotationMatrix2D函数获得变换矩阵
# 第一参数指定旋转圆点；第二个参数指定旋转角度；第二个参数指定缩放比例。
M=cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
dst=cv2.warpAffine(src,M,(rows,cols))

# 窗口大小不可以改变:cv2.WINDOW_AUTOSIZE
# 窗口大小可以改变:cv2.WINDOW_NORMAL
# 窗口大小自适应比例：cv2.WINDOW_FREERATIO
# 窗口大小保持比例：cv2.WINDOW_KEEPRATIO
# 显示色彩变成暗色：cv2.WINDOW_GUI_EXPANDED
cv2.namedWindow(wndName_1,cv2.WINDOW_FREERATIO)
cv2.imshow(wndName_1,src)

cv2.namedWindow(wndName_2,cv2.WINDOW_FREERATIO)
cv2.imshow(wndName_2,dst)

cv2.waitKey(0)