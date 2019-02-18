# -*- coding: UTF-8 -*- 
# 面向对象

# class 类
class School:
    var_ = '变量'

    def __init__(self,name):
        self.name = name
        print(name)

    def search(self):
        print('我是对象的方法 %s' % self.name)


# 默认会调用init方法  -----  传入参数
obj1 = School('清华') # 清华

# 调用对象方法
obj1.search() # 我是对象的方法  清华

# School.search()  # 会报错 没有传入 name 参数

# 打印变量
print(School.var_) # 变量

# 打印方法
# print(dir(School))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'search', 'var_']

# 查看类的属性
# print(School.__dict__)


# 静态属性   调用的时候不用加 （）
class Meth:
    def __init__(self):
        print('over')

    @property
    def vartrol(self):
        # print('直接属性调用')
        return '数据'  # 也可以返回表达式

ms = Meth()  #over
# ms.vartrol  #直接属性调用
print(ms.vartrol)  # 数据



# 类 方法 ------- 用类直接执行方法 而不需要 实例化

class A:
    a = 1

    def __init__(self,name):
        self.name = name

    @classmethod
    def test1(cls):
        print(cls,cls.a)  # cls就是类名 也可以叫self 占位的意思

A.test1() # <class '__main__.A'>  1


# 静态方法 --- 没法调用类变量 类属性  ---- 是类的工具包

class B:
    a = 1

    def __init__(self,name):
        self.name = name

    @staticmethod
    def test(name):   # 不跟任何绑定 相当于定义个外部的函数
        print(name)

    def test1(name):  # 这种定义的方法毫无意义
        print(name)

B.test('xiaoming')  # xiaoming

B.test1('xiaohong')  # xiaohong  类名调用可以

b = B('lili')
# b.test1('lili')  #  实例化后调用会报错 因为会把实例b传进去 就是self
b.test('lili')  # 正常打印  ----- 使用 staticmethod







