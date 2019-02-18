# -*- coding: UTF-8 -*- 
# 元组
tu = (1,2,3,4,5,)
print(tu[0],tu[0:2])  # 元组可以索引取值  但是不可以被修改和增加或者删除

tut = (1,2,3,([(1,2,3)],),)
tut[3][0][0] = 111  # 元组的一级元素不可修改  但是一级元素的内部元素的 列表中元组 可以修改
print(tut)

for item in tu :   # 元组是可迭代对象
    print(item)

st = 'nihaoxiaoming'
print(tuple(st))   # 字符串转换元组

li = [1,2,3,4,5]
print(tuple(li))  # 列表转换元组

tus = (1,2,3,4,)
print(list(tus))  # 元组转换成列表

tu_ = ('1','2','3','4',)
res = "_".join(tu_)
print(res)  # 元祖转字符串 只限于 元组是字符串

lis = [1,2,3]
lis.extend((4,5,6,))  # 元组也可扩展到列表里
print(lis)

lisss = (1,2,3,3,3,3,)
print(lisss.count(3))  # 元素出现的个数
print(lisss.index(2))  # 元素出现的位置






