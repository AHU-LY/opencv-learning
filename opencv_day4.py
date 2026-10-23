import cv2
img=cv2.imread('test.png')

#高斯核大小的影响
g5=cv2.GaussianBlur(img,(5,5),0)    #blur:模糊；尺寸用的是，不是*
g31=cv2.GaussianBlur(img,(31,31),0)

cv2.imshow('Gaussian 5*5',g5)
cv2.imshow('Gayssian 31*31',g31)
cv2.waitKey(0)
cv2.destroyAllWindows()

#中值滤波和高斯滤波的对比
import numpy as np
noisy=img.copy()
for _ in range(2000):   #range(2000)生成0-1999的整数序列，这句话就是把下面的执行2000遍
    y,x=np.random.randint(0,noisy.shape[0]),np.random.randint(0,noisy.shape[1])
    noisy[y,x]=[255,255,255] if np.random.rand()>0.5 else[0,0,0]

gauss_denoise=cv2.GaussianBlur(noisy,(5,5),0)
median_denoise=cv2.medianBlur(noisy,5)

cv2.imshow('Noisy',noisy)
cv2.imshow('Gaussian',gauss_denoise)
cv2.imshow('Median',median_denoise)
cv2.waitKey(0)
cv2.destroyAllWindows()

#将高斯滤波加入Pepline
img_blur=cv2.GaussianBlur(img,(5,5),0)
hsv_img = cv2.cvtColor(img_blur, cv2.COLOR_BGR2HSV)

cv2.imshow('Original', img)
cv2.imshow('HSV', hsv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

lower_bound = (30, 50, 50) 
upper_bound = (100, 255, 255)
mask = cv2.inRange(hsv_img, lower_bound, upper_bound)

cv2.imshow('Mask Result', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 5. 找白块的轮廓（cv2.RETR_EXTERNAL 表示只找最外层，cv2.CHAIN_APPROX_SIMPLE 压缩边界）
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 6. 复制原图用来画框
result_img = img_blur.copy()

# 7. 遍历找出来的每一个轮廓
for cnt in contours:
    # 计算包围轮廓的最小矩形框 (x, y, w, h)
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(result_img, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow('Detected', result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()