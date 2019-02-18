# -*- coding: UTF-8 -*- 
# 多态 ------- 对象通过他们共同的属性和动作来操作及访问，而不需要具体的类

class Charge:
    def __init__(self):
        pass

    def res(self):
        print('over')


class A(Charge):
    pass

class B(Charge):
    pass

class C(Charge):
    pass

a1 = A()
b1 = B()
c1 = C()

def func(obj):
    obj.res()

# 通过函数来实现 对象的共同方法 --- 统一接口 共同实现
func(a1)





