import cv2
import numpy as np

color=cv2.imread("../lena.jpg",1)
gray=cv2.imread("../lena.jpg",0)

print("图像Gray属性：")
print("gray.shape:",gray.shape)
print("gray.dtype:",gray.dtype)
print("gray.size:",gray.size)

print("图像color属性：")
print("color.shape:",color.shape)
print("color.dtype:",color.dtype)
print("color.size:",color.size)


