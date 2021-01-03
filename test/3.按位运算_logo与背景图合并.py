import cv2
import numpy as np
# load图像
src = cv2.imread('starnight.png')
logo = cv2.imread('logo09.jpg')

# 1.把logo放到图像左上角
#把logo图的宽与高取出来，形成roi感兴趣区域
rows, cols = logo.shape[:2]# shape方法返回图片的分辨率，高度和宽度
roi = src[:rows,:cols]# 第0行到rows行，第0列到cols列的区域设定为roi（即感兴趣区域）


# 2.创建logo的掩码
logoGray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)#灰度转换
# 当像素值高于阈值时，我们给这个像素赋予一个新值（可能是白色），
# 否则我们给它赋予另一种颜色（也许是黑色）,threshold()
# cv2.THRESH_BINARY,cv2.THRESH_BINARY_INV,cv2.THRESH_TRUNC,cv2.THRESH_TOZERO,cv2.THRESH_TOZERO_INV
ret,mask = cv2.threshold(logoGray, 100, 255, cv2.THRESH_BINARY)#大于200的像素，改成255


# 3.逆掩码(背景白，logo黑)
mask_inv = cv2.bitwise_not(mask)# 非运算，（图片文件），将图片里像素值按位反向


#4.背景图，感兴趣区域与mask_inv做与运算，得出新的roi区域
src_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)# 与运算，(目标文件，源文件，mask)，将图片里的像素值按位与


#5.logo图，loo图与mask做与运算，得出新的logo图
logo_fg = cv2.bitwise_and(logo, logo, mask=mask)


#6. 把前景和背景合并
dst = cv2.add(src_bg, logo_fg)
cv2.imshow("dst",dst)

# roi放入原图
src[:rows,:cols] = dst
# #显示
dd = np.hstack((src_bg,dst))
cc = np.hstack((mask,mask_inv))

cv2.namedWindow('res',cv2.WINDOW_NORMAL)
cv2.namedWindow('rses',cv2.WINDOW_NORMAL)
cv2.imshow('res',cc)
cv2.imshow('rses',dd)
cv2.imshow('最后的图',src)
cv2.waitKey(0)
cv2.destroyAllWindows()