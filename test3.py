#定义列表，存数值
nums=[12,5,27,8,19]
max=nums[0]
#比较出最值
for max1 in nums[1:]:
    if max1>max :
        max=max1
print(f'最大值是{max}')
        