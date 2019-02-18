# -*- coding: UTF-8 -*- 
# 元类例如： type 等


# 控制类的生成 ------

class Types(type):
    def __init__(self,a,b,c):
        print('元类的构造函数已经执行')
        print(a,b,c)
# Foo () {'__module__': '__main__', '__qualname__': 'Foo', '__init__': <function Foo.__init__ at 0x10087bea0>}

    def __call__(self, *args, **kwargs):  # 实例化后会触发
        print(args,kwargs)  # ('lili',) {}
        obj = object.__new__(self) # objject.__new__(Foo)  -> 产生f的
        self.__init__(obj,*args,**kwargs) # 传回去
        return obj

class Foo(metaclass=Types): # 相当于实例化一个类： Types('Foo',(obj),{})  ---  4个参数
    def __init__(self,name):
        self.name = name

f = Foo('lili')
print(f) # <__main__.Foo object at 0x10fc8aef0>
print(f.__dict__)  # {'name': 'lili'}









