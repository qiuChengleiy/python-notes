# -*- coding: UTF-8 -*-
# 类装饰器

def deco(obj):
    print('didiidid') # didiidid
    print(obj.__dict__)
    obj.name='lili'
    return obj

@deco  # A=deco(A)  ---- @ 是一个语法糖
class A:
    def test(self):
        print('tetetetete')

a = A()
print(a.name)  # lili

@deco
def test1():
    print('haha')


print(test1.__dict__)  # {'name': 'lili'}  --- 装饰器内部打印 {}



# 传参数形式装饰器
def Typed(**kwargs):
    def decos(obj):
        print('didiidid') # didiidid
        print(obj.__dict__)
        obj.name='lili'
        print(kwargs) # {'x': 1, 'y': 2, 'z': 3}
        for key,val in kwargs.items():
           # obj.key = val  这个最终返回的是 obj.key=3
            setattr(obj,key,val)  # 循环设置属性
            print(key)
        return obj
    return decos

@Typed(x=1,y=2,z=3)  # 传入参数
class B:
    def test(self):
        print('tetetetete')

b = B()
# print(b.name)  # lili
print(B.__dict__) # 最终有一个赋值到
# {'__module__': '__main__', 'test': <function B.test at 0x109ca10d0>, '__dict__': <attribute '__dict__' of 'B' objects>, '__weakref__': <attribute '__weakref__' of 'B' objects>, '__doc__': None, 'name': 'lili', 'key': 3}

# 高级用法


class Types:  # 描述符
    def __init__(self,key,expec_type):
        self.key = key
        self.expec_type = expec_type

    def __get__(self, instance, value):  # 非数据
        print('get',instance,value)  # get <__main__.B object at 0x10f96ef98> <class '__main__.B'>
        return instance.__dict__[self.key]  # 取值

    def __set__(self, instance, value):  #  数据 -- set <__main__.B object at 0x107f25f28> lili
        print('set',instance,value)
        if not isinstance(value,self.expec_type):  # 判断类型
            raise TypeError(self.expec_type)
            return
        instance.__dict__[self.key] = value  # 赋值


def ADD_Typed(**kwargs):
    def decos(obj):
        print(kwargs)
        for key,val in kwargs.items():
            setattr(obj,key,Types(key,val))   # 就相当于给类设置属性例如： name = Types('sss',str) --- 会触发set方法
        return obj
    return decos


@ADD_Typed(name=str,age=int)
class D:  # 代理类
    def __init__(self,name,age):
        self.name = name  # 会触发set
        self.age = age

d = D('xiaoming')
# d = D('hahahaha','ss') # 报错
print(D.__dict__)







