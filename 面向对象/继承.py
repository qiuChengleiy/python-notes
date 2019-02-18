# -*- coding: UTF-8 -*-

# 继承 ------- 当类之间有很多相同的功能时，提取这些共同的功能做成基类，用继承
# 1. 派生继承 ----- 代码重用 方法继承
# 2. 接口继承 -----  子类继承接口 并且实现接口定义的方法
# 3. 继承顺序 ----- 深度优先（经典类） 广度优先 （新式类 -- Py3）

class A:
    name = 'lili'

    def __init__(self):
        print('A')  # A

    @classmethod
    def m1(self,name):
        print(name)
class B:
    def __init__(self):
        print('A')  # A

    @classmethod
    def m2(self, name):
        print(name)

class C:
    def __init__(self):
        print('A')  # A

    @classmethod
    def m3(self, name):
        print(name)


# 单继承
class Extend(A) :
    def __init__(self):
        pass

e = Extend()
print(e.name)  # lili
e.m1('lili') # lili


# 多继承 ------ 就是把类名传进去
class Extends(A,B,C) :
    def __init__(self):
        pass


Extends.m1('1')  # 1
Extends.m2('2')  # 2
Extends.m3('3')  # 3


# 接口继承 --- 定义一个基类 用abc模块抽象方法 把自己的方法定义成接口函数 用子类继承它 并实现它内部的方法，如果不实现会报错 没法实例化
# 基类 ---- 不需要实现内部方法 只需要定义接口函数
# 接口 ->  就是一个函数
# 好处 ---- 归一化设计


import abc
class Basic(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def test1(self):
        pass

    @abc.abstractmethod
    def test2(self):
        pass



class Childs(Basic):
    def __init__(self):
        pass

    def test1(self):
        print('t1')

    def test2(self):
        pass

c = Childs()  # 如果内部不实现方法会报错



# 继承顺序
# 怎么实现继承的？
# 对于定义的每一个类 py会计算出一个方法解析顺序--MRO，这个MRO列表就是一个简单的所有基类的线性顺序列表



class E:
    name = 'lili'

    def __init__(self):
        print('A')  # A

    def m1(self,name):
        print(name)
class F:
    pass

class G:
    pass

class H:
    pass

class I:
    pass


