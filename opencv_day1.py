import cv2
import numpy as np
# 1. 读取图像（注意路径别写错）
img = cv2.imread('test.png')

# 2. 打印它的 shape，验证它是不是一个 numpy 数组
print("图像形状:", img.shape) 

# 3. 把它变成灰度图（三维变二维）
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("灰度图形状:", gray.shape)

# 4. 用窗口显示出来看看
cv2.imshow('Original', img)
cv2.imshow('Gray', gray)

# 5. 等待按键，按任意键关闭窗口（千万别漏了这句，否则窗口会卡死）
cv2.waitKey(0)
cv2.destroyAllWindows()