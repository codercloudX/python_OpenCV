import cv2 
import numpy as np

img1=np.ones((3,4),dtype=np.uint8)*100
img2=np.ones((3,4),dtype=np.uint8)*10
gamma=3

#加权和运算：
#src*alpha+src2*beta+gamma
#alpha是src1的系数，beta是src2的系数，gamma是亮度调节值
img3=cv2.addWeighted(img1,0.6,img2,5,gamma)
print(img3)

