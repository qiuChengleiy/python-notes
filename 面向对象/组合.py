# -*- coding: UTF-8 -*-

# 组合 ------ 当类之间有显著不同，并且较小的类是较大的类所需要的组件时，用组合方式

class A:
    name = 'lili'

    def __init__(self):
        print('A')  # A

    def m1(self,name):
        print(name)
class B:
    pass

class C:
    pass


class All:
    def __init__(self):
        self.a = A()    # 实例化的过程会执行上面的代码
        self.b = B()
        self.c = C()


    def pr(self):
        self.a.m1(self.a.name)     # 可以拿到 A中的属性和方法


all = All()
all.pr()





























