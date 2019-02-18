# -*- coding: UTF-8 -*- 
# json 模块
import json
dic = {"name": "lili"}

# 转成json字符串   都是双引的
data = json.dumps(dic)

# json.dump()  一般用于文件处理  --- 写入文件

print(data)  # {"name": "lili"}
print(type(data))  # <class 'str'>

# 字符串转成 数据类型
pre = json.loads(data)
print(pre)  # {'name': 'lili'}
print(type(pre))  # <class 'dict'>

# json.load()  用于文件处理 ---  读取文件











