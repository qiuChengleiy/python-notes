# -*- coding: UTF-8 -*-

# item的前提是 obj[key]
class A:
    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        print(key,value)
        self.__dict__[key] = value  # 反射到类上 --- 设置属性

    def __delitem__(self, key):
        self.__dict__.pop(key)

a = A()
print(a.__dict__)  # 当没有定义__init__方法时 是个 {}空的

a['name'] = 'lili' # name lili  ---- 会触发setitem属性
print(a.name) # -- 如果没反射 报错 因为name属性没有反射上去

del a['name']
print(a.__dict__)

a['age'] = 20
print(a['age'])  # 20



