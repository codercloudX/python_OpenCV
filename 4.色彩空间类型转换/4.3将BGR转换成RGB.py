import numpy as np
import cv2

img =np.random.randint(0,255,size=[2,4,3],dtype=np.uint8)
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
bgr=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

cv2.imshow("img",img)
cv2.imshow("rgb",rgb)
cv2.imshow("bgr",bgr)

print("img:",img)
print("rgb:",rgb)
print("bgr:",bgr)


cv2.waitKey(0)
cv2.waitKey(0)