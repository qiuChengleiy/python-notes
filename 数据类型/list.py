# -*- coding: UTF-8 -*- 
li = [1,2,3,4,4,5,5]
print(li[2])
print(li[4:-2])  # 列表也有切片

for item in li :
    print(item)

# 修改和删除都可以以 区间的形式

li[3] = 'hello'
print(li)   # 列表的值可以被改变

del li[0]  # 删除   也可以有区间的形式
print(li)

print(1 in li)  # 支持 in 操作符

# 字符串换列表    注意： 数字不能转换
lis = list('sdsadasdsadadasda')
print(lis)  # ['s', 'd', 's', 'a', 'd', 'a', 's', 'd', 's', 'a', 'd', 'a', 'd', 'a', 's', 'd', 'a']

# 列表转字符串  先转后加
liss = [1,2,3,4,5,'wewq']
strs = ''
for i in liss :
    strs += str(i)
print(strs)

li2 = ['1','3','4']
print(''.join(li2))   # 只限于字符串的列表

li2.append(['s',1,3])  # 尾部添加
print(li2)

li2.clear()
print(li2)  # 清空列表

li3 = li2.copy()  # 浅拷贝
print(li3)

li_ = [1,2,3,4,4,5]
print(li_.count(4))  # 计算元素出现的次数

# 传的是可迭代对象
li_.extend(['1',3,66])   # 将元素扩展到列表里 与 append不同 append不会扩展 只是添加
print(li_)  # [1, 2, 3, 4, 4, 5, '1', 3, 66]

print(li_.index(4)) # 找出元素的位置  从左往右

li_.insert(1,'hhhh')  # 在1的位置插入 指定元素
print(li_)

vs = li_.pop()   # 在尾部删除元素 并且 可以获取到被删的元素
print(vs, li_)

vs1 = li_.pop(1)  # 删除指定索引
print(vs1 , li_)

li_.remove(3) # 删除列表中指定的第一个值 左边优先
print(li_)

li_.reverse()  # 列表反转
print(li_)

sor = [1,5,2,6,22,12]
sor.sort()  # 排序 从小到大
print(sor)
sor.sort(reverse=True)  # 反转排序 [22, 12, 6, 5, 2, 1]
print(sor)







