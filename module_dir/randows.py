# -*- coding: UTF-8 -*- 
# 随机数模块
import  random

ret = random.random()   # 0-1范围内
print(ret) # 0.48524753451551383

print(random.randint(1,3))  # 1-3范围内的随机整数 包含1和3
print(random.randrange(1,4)) # 同上

print(random.uniform(1,3))  # 1-3内的范围 包含小数

print(random.choice([1,2,3,9,'1']))  #对可迭代对象的随机取

print(random.sample([1,10,8,8,2],2))  # 随机取两个  [8, 2]

re = [1,2,3,4,5]
random.shuffle(re)   # 随机打乱
print(re)  # [5, 1, 4, 2, 3]