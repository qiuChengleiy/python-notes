# -*- coding: UTF-8 -*-
# 封装  ---- 外部访问不到
# 真正意义的封装： 明确区分内外，内部的实现逻辑，外部无法知晓，并且为封装到内部的逻辑提供一个访问接口给外部使用

# _  开头的是私有的
# __ 开头的会自动重新命名 _类名__属性名

class A:
    __name = 'lili'   # __ 表示隐藏的  如果没必要隐藏的最好不要隐藏

    def __init__(self):
        pass

    @classmethod
    def __test(self):
        print('__',self.__name)  # 内部可以访问

    def interface(self):  # 可以提供对外的接口
        pass


A._A__test() # __
# A.__test()  访问不到






