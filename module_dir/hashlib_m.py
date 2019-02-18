# -*- coding: UTF-8 -*- 
# hashlib 模块  摘要算法
import hashlib


m = hashlib.md5()  # 有时候会撞库 比如网站有解密的
m = hashlib.md5('dslkjlajdal'.encode('utf8'))   # 最好是依据某一个字符串来进行加密
m.update('hello'.encode('utf-8'))

# 得到密文   ----  md5 转不回 明文   ： 当用户登录的时候  密码转密文和数据库的密文比较
print(m.hexdigest()) # 5d41402abc4b2a76b9719d911017c592 (32位)

# 如果再次update 会连同之前的字符串一起加密


m = hashlib.sha256()  # sha256算法  消耗的时间会多一些

m.update('hello'.encode('utf-8'))


print(m.hexdigest()) # 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824 （64位）

# PY也有其它算法。。。。。

