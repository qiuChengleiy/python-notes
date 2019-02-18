# -*- coding: UTF-8 -*- 
name = 'xiaohong'
res = 'yes' if name == 'xiaohong' else 'no'  # 判断对 返回前边的 否则 返回后边的
print(res)

# 列表解析
list = ['鸡蛋%s' %i for i in range(5)]   # 生成器表达式更省内存
print(list) # ['鸡蛋0', '鸡蛋1', '鸡蛋2', '鸡蛋3', '鸡蛋4']
list = ['鸡蛋%s' %i for i in range(5) if i == 3]
print(list)  # ['鸡蛋3']








