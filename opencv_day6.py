import cv2
import numpy as np
img=cv2.imread('test.png')
hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower=(30,50,50)
upper=(100,255,255)
mask=cv2.inRange(hsv_img,lower,upper)
kernel=np.ones((5,5),np.uint8)
erosion=cv2.erode(mask,kernel,iterations=1)#腐蚀erode：让图像里的白色区域变瘦（缩小）,用来去掉背景上细小的白色噪点（灰尘），断开粘连在一起的物体
dilation=cv2.dilate(mask,kernel,iterations=1)#膨胀dilate:让图像里的白色区域变胖（扩大）,用来把断裂的线条连上，把目标区域变大
cv2.imshow('mask',mask)
cv2.imshow('erosion',erosion)
cv2.imshow('dilation',dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)#开运算 = 先腐蚀后膨胀。专门用来去噪（去毛刺，大物体保留，小噪点消失）
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)#闭运算 = 先膨胀后腐蚀。专门用来填洞（把物体内部的小黑洞填满）
cv2.imshow('opening',opening)
cv2.imshow('closing',closing)
cv2.waitKey(0)
cv2.destroyAllWindows()