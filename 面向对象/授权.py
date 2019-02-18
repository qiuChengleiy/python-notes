# -*- coding: UTF-8 -*-

# 授权 --- 包装的一个特性，可以删除、新建、修改原有的产品的功能
# 方式： 组合
# 关键：  __getattr__


class Open:
    def __init__(self,filename,mode='r',encoding='utf-8'):
        self.file = open(filename,mode,encoding=encoding)
        self.mode = mode
        self.encoding = encoding

    def __getattr__(self, item):
        print(item)  # 打印属性名
        # 定制read方法
        return getattr(self.file,'read','read_method')  # 实际上把file对象的属性和方法都继承到了

    # def read(self):
    #     pass
    #
    # def write(self):
    #     pass


# 定制Open ----  1.继承实现  --- 2.授权
f = Open('a.txt','w')
print(f.read) # <built-in method read of _io.TextIOWrapper object at 0x1058ce708>

# f.write也可以

# f.tell # tell



