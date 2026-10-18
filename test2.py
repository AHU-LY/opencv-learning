#1.定义字典，存三个同学
d={'小明':18,'小红':19,'小刚':20}

#2.输入名字
name=input()

#3.判断名字在不在字典里面在或不在分别输出
if name in d:
    print(f'{name}今年{d.get(name)}')
else:
    print('不在字典里')
