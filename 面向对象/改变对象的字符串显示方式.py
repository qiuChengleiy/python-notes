# -*- coding: UTF-8 -*-
# 修改系统默认的字符串形式

class A:
    year = '2019'
    mon = '1'
    day = '14'
    def __init__(self,name):
        self.name = name

    def __str__(self):   #  str()
        return 'name is lili'

    def __repr__(self):  # repr
        return 'repr is repr'

    def __format__(self, format_spec): #
        print('字符串格式化')
        if not format_spec:  #判断是否为空或者是否存在于某一个字典里
            format_spec = 'ymd'
        fm = format_spec  # 可能是字典类型 具体情况而定
        return fm.format(self)


a = A('lili')
print(str(a)) # name is lili
print(a.__str__()) # name is lili

# 在解释器中有用
print(repr(a)) # repr is repr
print(a.__repr__()) # repr is repr

print(format(a,'{0.year}-{0.mon}-{0.day}'))  #  2019-1-14----- 调用format方法
# {0.year}-{0.mon}-{0.day}


















