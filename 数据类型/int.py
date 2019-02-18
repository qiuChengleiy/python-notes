# -*- coding: UTF-8 -*-
a = "123"
print (type(a))

b = int(a)   # 整形转换
print (type(b),b)

c = int(a, base=16) # 进制转换
print (c)

# 字符串转为二进制
def encode(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])

# 二进制转为字符串
def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])

print(encode('hello'))
# 1101000 1100101 1101100 1101100 1101111

print(decode('1101000 1100101 1101100 1101100 1101111'))
# hello


num = 222
print (num.bit_length()) # 8    至少用几位二进制表示



