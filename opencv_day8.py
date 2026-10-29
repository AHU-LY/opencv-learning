import cv2
import numpy as np

#1.读取两张图
img1=cv2.imread('test1.jpg')
img2=cv2.imread('test2.jpg')

#2.转灰度（SIFT默认吃灰度）
gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

#3.创建SIFT探测器
sift=cv2.SIFT_create()

#4.寻找关键点（keypoints）和计算描述子（descriptors）
kp1,des1=sift.detectAndCompute(gray1,None)
kp2,des2=sift.detectAndCompute(gray2,None)

#5.画图：把找出来的关键点画在图上看看
img1_kp=cv2.drawKeypoints(img1,kp1,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
img2_kp=cv2.drawKeypoints(img2,kp2,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
img1_kp=cv2.resize(img1_kp,(600,600))
img2_kp=cv2.resize(img2_kp,(600,600))
cv2.imshow('Keypoints1',img1_kp)
cv2.imshow('Keypoints2',img2_kp)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 6. 创建 BFMatcher（暴力匹配器），对比两张图的指纹
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

# 7. 进行匹配
matches = bf.match(des1, des2)

# 8. 按照匹配的相似度排序
matches = sorted(matches, key=lambda x: x.distance)

# 9. 把匹配结果画出来
result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:20], None, flags=2)
result=cv2.resize(result,(600,600))
cv2.imshow('Matches', result)
cv2.waitKey(0)
cv2.destroyAllWindows()