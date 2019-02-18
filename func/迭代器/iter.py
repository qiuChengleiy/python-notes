# -*- coding: UTF-8 -*- 
strs = 'hello'
iter_strs = strs.__iter__()

# 迭代器有next方法  如果碰到异常会报错  for循环内部调用的也是next方法  可迭代对象包含文件对象
for i in range(4) :
    print(iter_strs.__next__())

# 也可以用系统提供的
#  next(iter_strs)

# 如果是字典 调用next得到的是key值
dics = {"k1": "v1","k2": "v2"}
iter_dics = dics.__iter__()

for i in range(3) :
    try:                    # 异常捕捉 防止程序崩溃
        print(iter_dics.__next__())   # k1  k2
    except StopIteration:
        print('迭代完毕')
        break
