# -*- coding: UTF-8 -*-
# 反射  ----- 自己检查自己  判断对象或类  -- PY一切皆对象
# 三个方法

class A:
    name = 'lili'
    def __init__(self):
        pass

# 在调用别人的类的时候 需要判断下是否有要定义的属性和方法
print(hasattr(A,'name'))  # True  判断是否有name属性  ---  如果没有返回 False

print(getattr(A,'name')) # lili  找到属性 可以返回结果  --- 没有 直接报错
print(getattr(A,'namesdada','没有这个属性')) # 可以设置默认值

setattr(A,'age',11)  # 设置属性 --- 也可以修改属性
print(A.age)  # 11

# 添加方法
setattr(A,'add',lambda x:x+1)
print(A.add(1))  # 2

# 删除属性
# del A.age
# print(A.age)  # 报错


# 下划线开头的
class B:
    name = 'lili'
    def __init__(self,d):
        self.d = d

    def __getattr__(self, item):  # 当没有这个属性的时候会调用这个方法
        print('根本不存在这个属性')

    def __delattr__(self, item): # 当删除没有这个属性的时候会调用这个方法  ---
        print('删除操作')

    def __setattr__(self, key, value):  # 设置属性就会触发 包括实例化的时候 --- obj.x赋值也会 ，如果这个方法不写 默认也会调用，但是不存在会报错
        print(key,value)    # d  20
        self.__dict__[key] = value  # 设置属性
        # 如果直接 self.key = value  会触发无线递归


b = B(20)
b.age  # 根本不存在这个属性
del b.huhu
print(b.__dict__) # {'d': 20}



class C:
    name = 'lili'
    def __init__(self):
        pass

    def __getattr__(self, item):
        print('attr')   # 还是触发attribute

    def __getattribute__(self, item):
        print('attribute')   # 属性有或者没有都会触发
        raise AttributeError('抛出属性异常')  # 抛出异常 ---只能抛出属性异常才会执行--- 下边可以执行attr 不管属性有没有都会去执行attr


c = C()
#c.name    # attribute
#c.age     # attribute