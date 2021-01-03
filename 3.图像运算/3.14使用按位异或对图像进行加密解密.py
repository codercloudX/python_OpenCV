import cv2 
import numpy as np



lena=cv2.imread("../lena.jpg",0)
cv2.imshow("lena",lena)
rows,cols=lena.shape

#1.构造用于作为密钥的图像，大小与源图像要一致
key=np.random.randint(0,256,size=[rows,cols],dtype=np.uint8)
cv2.imshow("key",key)

#2.将key与源图像进行异或运算，得出加密后的图像
dst=cv2.bitwise_xor(lena,key)
cv2.imshow("encryption",dst)

#3.将加密后的图像与key进行异或运算，得出源图像
src=cv2.bitwise_xor(dst,key)
cv2.imshow("dencryption",src)

cv2.waitKey(0)

