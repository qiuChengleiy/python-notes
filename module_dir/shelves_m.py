# -*- coding: UTF-8 -*- 
# shelve 模块

import  shelve
f = shelve.open(r'a.txt')

print(f) # <shelve.DbfilenameShelf object at 0x101cefe80>

# 将字典写入文件
f['stu1'] = {'name': 'lili','age': 20}

f.close()

# print(f.get('stu1')['name'])



