# -*- coding: UTF-8 -*-
# 描述符：
# 1.描述符本身定义成新式类，被代理的类也应该是新式类
# 2.必须把描述符定义成这个类的属性，不能定义到构造函数中
# 3.优先级： 类属性->数据描述符->实例属性->非数据描述符->找不到触发__getattr__()

# 可以用于传入的数据类型检测

class A:  # 描述符
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

    def __delete__(self, instance):
        print('delete')
        instance.__dict__.pop([self.key])

class B:  # 代理类
    name = A('name',str)  # 数据描述符 --- 属性 -- 期望的数据类型

    def __init__(self,name):
        self.name = name  # 会触发set

b = B('lili') # 触发set
b.name # 触发 get
b.name = 'xiaohong'  # 没有做真正的设置
print(b.name)  # None  ---- 赋值后 --xiaohong
# del  触发 delete
