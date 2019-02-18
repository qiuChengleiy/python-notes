# -*- coding: UTF-8 -*- 
# 集合

tu = (1,2,3,4,5)
print(type(tu))

# set 是可变集合 可以做操作
sets = set('nihao')  # 集合是无序的  只能存放不可变类型的值  重复的会被去掉
print(type(sets),sets)  # <class 'set'> {'i', 'a', 'n', 'h', 'o'}

forzen = frozenset('nihao')  # 不可变集合 不能操作
print(forzen)


set1 = set(['1','2','hhahaha','ss','ss'])
print(set1)  # {'2', 'hhahaha', '1', 'ss'}

s1 = set("xiaoming")
s1.add('20')   # 添加   只能是一个值
print(s1)

s1.clear()  # 清空
print(s1)

s1.copy() # 拷贝

s1.add('999')
s1.add('000')
s1.add('222')
s1.pop()  # 删除  随机删除
print(s1)

s1.remove('000')  # 删除指定  如果不存在会报错
print(s1)

s1.discard('888') # 删除指定 如果不存在 不会报错
print(s1)

v = list(s1)  # 集合转列表   传入的是可迭代类型
print(v)

#集合可以去重 但是也会把重复的去掉

xm = ['xiaoming','xiaohong','xiaoli']
xg = ['xiaoming','xiaohong','lili']
s1s = set(xm)
s2s = set(xg)

results = s1s.intersection(s2s)   # 取交集
results2 = s1s&s2s  # 效果同上  取交集
print(results,results2)  # {'xiaohong', 'xiaoming'}

results3 = s2s|s1s    # 取并集
results4 = s1s.union(s2s)
print(results3, results4)  #  {'lili', 'xiaoli', 'xiaoming', 'xiaohong'}

results5 = s1s-s2s    # 取差集  存在于s1s
results6 = s2s-s1s    # 取差集  存在于s2s
results7 = s1s.difference(s2s)
print(results5,results6,results7)  # {'xiaoli'}    ----     {'lili'}  -----  {'xiaoli'}


# 交叉补集
results8 = s1s.symmetric_difference(s2s)  # 先合并减去公用的部分
results9 = s1s^s2s # 同上
print(results8 ,results9)  # {'lili', 'xiaoli'}

# 差集更新
results10 = s1s.difference_update(s2s)   # 取完值后直接更新s1s
print(s1s)  # {'xiaoli'}
s1s = s1s-s2s
print(s1s)  # {'xiaoli'}


# 判断是否有交集
bools = s1s.isdisjoint(s2s)
print(bools)

# 判断是否包含于某个集合
ins = s1s.issubset(s2s)
print(ins)   # False

# 判断是否包含某个集合
outs = s1s.issuperset(s2s)
print(outs)   # False


# 集合更新    并集并不会更新集合
s1s.update(s2s)
print(s1s)


