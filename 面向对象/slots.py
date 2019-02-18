# -*- coding: UTF-8 -*-
# 类变量 --- 使得每一个实例不再具有__dict__属性
# 优势--省内存
class A:
    '这是一个类'
    __slots__ = ['name','age']  # --- {name:None,age:None}  意味着只能定义这几个属性


a = A()
a.name = 'lili'
print(a.name)
# a.sex = 'nan'  # AttributeError: 'A' object has no attribute 'sex'
# print(a.__dict__) # AttributeError: 'A' object has no attribute '__dict__'


# 补充： 类的描述信息  --- 该属性无法被继承
print(A.__doc__) # 这是一个类

# __module__是查看来自哪个模块

# __del__   析构函数 ----有py解释器 垃圾回收时会执行一般不用定义
class D:
    name = 'll'
    def __del__(self):
        print('执行了')

    def __call__(self, *args, **kwargs):
        print('执行了',*args)


d = D()
# del d.name
# del d   # 删除整个实例会执行

d('haha') # 执行了 haha  ---- 调用d下面的__call__方法




