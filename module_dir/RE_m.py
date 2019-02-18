# -*- coding: UTF-8 -*- 
# RE 正则模块
import re

# 完全匹配
strs = 'sdnasldaslkda'
res = re.findall('as',strs)
print(res) # ['as', 'as']

# 模糊匹配

# 元字符
st1 = "abbsdadasacccacds"

# 以 a开头s结尾 中间两个任意字符的 字符（几个点就是几个字符）
print(re.findall('a..s',st1))  # ['abbs', 'adas']

# ^  表示只能从字符串的开头开始找 必须开头是a...
print(re.findall('^a..s',st1))  # ['abbs']


# $  表示只能从字符串的结尾结束 必须结尾是 ...s
print(re.findall('a..s$',st1))  # ['acds']

# \  表示 转义

# | 管道符   或





# 当大量重复的时候
# * 表示 0-无穷大   ==>  {0,}
# + 表示 1-无穷大   ==>  {1,}
# ? 表示 0-1       ==>  {o,1}
#
#  {}  区间 ---
#      {6,}  表示 6 到无穷
#  {6} 表示 重复 6次

st2 = "ddddddsdsadsalddddddddddasiiiowoqqdddddd"
print(re.findall('d*',st2)) # ['', 'd', '', '', 'd', '', '', '', 'dddddddddd', '', '', '', '', '', '', '', '', '', '', '']
print(re.findall('^d*',st2)) # ['dddddd']
print(re.findall('d*$',st2)) # ['dddddd', '']
print(re.findall('^d*$',st2)) # []

# 也叫贪婪匹配
print(re.findall('d+$',st2)) # ['dddddd']

st3 = 'asdasdsadaalexxxxx'
print(re.findall('alex+',st3))  # ['alexxxxx']

# 惰性匹配 加个 ？
print(re.findall('alex?',st3)) # ['alex']

print(re.findall('10{8}','1000000000')) # ['100000000']  结果是8位  字符串是9位  表名是匹配了 8个0


#  ****************重点********************

# []  字符集 存放后边可能匹配到的字符        在字符集里的特殊符号例如 * 就是普通字符了
# [] 里的功能字符
# -   例如 a-z  表示26个英文  0-9 表示数字  A-Z表示大写
# ^   例如： [^a-z] 表示匹配 a-z之外的字符
# \

st4 = 'xyzsdalksdkladaxym'
print(re.findall('xy[zam]',st4))  # ['xyz', 'xym']

st5 = '789a9asxzcaas'
print(re.findall('[a-z]',st5)) # ['a', 'a', 's', 'x', 'z', 'c', 'a', 'a', 's']
print(re.findall('[a-z]*',st5)) # ['', '', '', 'a', '', 'asxzcaas', '']
print(re.findall('[a-z]*?',st5)) # ['', '', '', '', 'a', '', '', 'a', '', 's', '', 'x', '', 'z', '', 'c', '', 'a', '', 'a', '', 's', '']

print(re.findall('[A-Z]',st5)) # []

print(re.findall('[0-9]a*',st5)) # ['7', '8', '9a', '9a']

print(re.findall('9[^a-z]',st5)) # []

# 匹配括号 (2-1)
cal = "12+3+(2+3+4*(2-1))"
print(re.findall('\([^()]*\)',cal))  # ['(2-1)']


# \ 关于反斜杠
# \d  ===>  0-9
# \D =====>  [^0-9]  表示非数字部分
# \s  ------  匹配任何空白字符   相当于  [\t\n\r\f\v]
# \S  -------  匹配任何非空白字符     [^\t\n\r\f\v]
# \w ------  匹配任何 字母 数字 字符   [a-zA-Z0-9]
# \W ------- 匹配任何非 数字 字母    [^a-zA-Z0-9]
# \b  ------  匹配特殊字符边界  如:  空格 & #

print(re.findall('[\d]','01')) # ['0', '1']  匹配0或1

# 对于空格
print(re.findall(r'n\b','hello n hanha'))  # ['n'] 加上r 表示普通字符
print(re.findall('n\\b','hello n hanha'))  # ['n'] 加上 \



#  |  ---- 或
print(re.findall('aa|b','aabbcc'))  # ['aa', 'b', 'b']


# 分组 （） 会先把分组的找出来  去掉优先级 ---- (?:
print(re.findall('(abc)+','abcabcbacbacbacbabcbacbac')) # ['abc', 'abc']

# 语法 --- '(?P<name>写自己想要匹配的字符)'  name的作用就是方便最后拿到分组的结果
print(re.findall('(?P<name>\d+)','ab99cc00ccc')) # ['99', '00']

# search 匹配成功返回对象   不成功也不会报错  而且只会返回一个结果
print(re.search('(?P<name>\w+)','abccccc'))
print(re.search('(?P<name>\d+)','abc9009hh55cccc').group())  # 拿到结果 9009

# 拿到分组name的值
print(re.search('(?P<name>[a-z]+)\d','abc9009hh55cccc').group('name'))  # 拿到结果 abc

# 补充:
print(re.findall('www\.(baidu|163)\.com','www.baidu.com')) # ['baidu']
# 去掉优先级
print(re.findall('www\.(?:baidu|163)\.com','www.baidu.com')) # ['www.baidu.com']



#  正则模块的方法
# findall()  略
# search()  略

# match 判断是否匹配成功 成功 .group方法返回 1  失败没有group方法 返回 None
print(re.match('\d','aa'))  #

# split 分割
print(re.split('\d','a1c2s'))  # ['a', 'c', 's']

# sub 替换
print(re.sub('\d+','A','qwsadad11111sdasda')) # qwsadadAsdasda 贪婪匹配11111替换成A
print(re.sub('\d','A','dasda99999sdad')) # dasdaAAAAAsdad  会匹配每个数字换成A
print(re.sub('\d','A','dasda99999sdad',2)) # dasdaAA999sdad  只会匹2个数字换成A

# sub 替换 并返回次数
print(re.subn('\d+','A','qwsadad11111sdasda'))  # ('qwsadadAsdasda', 1)  匹配了一个


# compile 匹配规则  然后可以调用正则的方法  好处在于可以多次利用
com = re.compile('\d')
print(com.findall('sdad333dada33')) # ['3', '3', '3', '3', '3']

# finditer 返回迭代器对象
print(re.finditer('\d','sdsada999sdad9ad9ad9a')) # <callable_iterator object at 0x105ea3898>

#拿到结果
its = re.finditer('\d','sdsada999sdad9ad9ad9a')
print(next(its).group()) #9
print(next(its).group())  #9
print(next(its).group())  #9
print(next(its).group()) #9

