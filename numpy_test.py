import numpy as np
#创建1到12的一维数组，打印shape、ndim、dtype
arr1=np.arange(1,13)  #arr1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr1,arr1.shape,arr1.ndim,arr1.dtype)

#创建“假图像”240*320*3，类型unit8,打印shape和size
arr2=np.ones((240,320,3),np.uint8)
print(arr2,arr2.shape,arr2.size)

#创建【3，8，1，15，6，20，2】，输出大于5的元素
arr3=np.array([3,8,1,15,6,20,2])
print(arr3[arr3>5])  #布尔索引

#把1-12改为3*4矩阵，打印：第二行、第三列、右下角2*2子块
arr4=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr4[1],arr4[:,2],arr4[1:3,2:4],arr4[-2:,-2:])  #切片语法：arr[开始:结束, 开始:结束]（注意是左闭右开,可正可负）

#生成5*5单位矩阵，把对角线全部改成9并打印
arr5=np.eye(5)  #生成5*5的单位矩阵
for i in range(5):  #range(5):生成0，1，2，3，4
    arr5[i][i]=9
print(arr5)

#用linspace生成0到100的11个数，只取索引为偶数的元素打印
arr6=np.linspace(0,100,11)  #np.linspace(起点，终点，元素个数)
print(arr6[::2])
