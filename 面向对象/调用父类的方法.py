# -*- coding: UTF-8 -*- 
class A:
    def __init__(self):
        pass

    def test(self):
        print('super')

# super 调用父类

class B(A):
    def __init__(self):
        pass

    @classmethod
    def test(self):
        super().test(self)  # super
        print(self)  # <class '__main__.B'>

B.test()


















