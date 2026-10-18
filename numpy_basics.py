import numpy as np

#ndarry属性
arr=np.array([[1,2,3],[2,3,4]])
print(arr.ndim,arr.shape,arr.size,arr.dtype)    #输出维度、形状、总长度、元素类型

#强制统一类型
list1=[1,2,3,4.12]
list2=[1,2,3,4.12,'object']
print(np.array(list1).dtype,np.array(list2).dtype)  #list1强制为float,list2强制为Unicode

#routines的函数创建
print(np.ones(shape=(3,2),))



#基本运算原则：两个矩阵运算，就是对应位置的数据的运算
arr1=np.random.random(10)
arr2=np.random.randint(0,10,size=(10))
print(arr1,arr2,arr1+arr2)

#广播Broadcast规则：1.两个数组的后缘维度的轴长度相符，例：（3，2） （4，3，2）相符（从右往左）
#2.或其中的一方的长度为1    广播会在缺失和（或）长度为1的维度上进行
print(arr1>0.6)     #可以跟任意整数进行广播运算
a=np.ones((2,3))
b=np.arange(3)
print(a,b,a+b)
c=np.arange(3).reshape((3,1))
d=np.arange(3)
print(c,d,c+d)



#nadrray的聚合函数
#求和np.sum
data1=np.random.randint(0,100,size=5)   #一维
print(data1,data1.sum())
data2=np.random.randint(0,10,size=(3,2))    #二维
print(data2,data2.sum(),data2.sum(axis=0),data2.sum(axis=1))    #总和，行的和，列的和

#空值np.nan（not a number）
print(type(np.nan))     #numpy的空值是float型
data=np.random.randint(0,10,size=10)
data=data.astype(np.float32)    #转换成float型
data[1]=np.nan
print(data.sum())       #结果是nan,因为nan特性：nan和任意浮点数运算结果都是nan
newdata=np.nansum(data)     #np.nansum可以剔除nan进行运算
print(newdata)      

#最大小值np.max/np.min
arr3=np.array([1,2,3])
print(arr3.max(),arr3.min())

#any()和all()
data3=np.random.randint(0,2,size=10).astype(np.bool)
print(data3.any())       #存在一个true,返回true
print(data3.all())       #全是true,返回true
