import cv2
import numpy as np
#矩阵乘法
A=np.array([[1,2],[3,4]])   #矩阵对应位置元素相乘
B=np.array([[5,6],[7,8]])   #矩阵乘法
print(A*B,A@B)

#聚合与axis轴
arr=np.random.randint(0,10,(3,4))
print(arr,arr.sum(axis=0),arr.sum(axis=1))  #axis=0:列求和，axis=1:行求和



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