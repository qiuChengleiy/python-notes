# -*- coding: UTF-8 -*-
# 字符串一旦创建不可修改

name = "xiaoming"
name1 = "SDADSAD"
print (name.capitalize()) # 首字母大写

# str()  字符串转换
print (name1.lower()) # 小写（限于英文字符的转换） casefold()不限制  py3
lower = "sdadsada"
print(lower.islower())   # 判断是否是小写

print(name.upper()) # 转换成大写
print(name.isupper()) # 判断是否是大写

names = "nihaoJULICE"
print(names.swapcase())  # 大小写转换

print (name.center(10)) # 一共10个字符长度 name 放中间
print (name.center(10,'&'))  # 其余位置用&代替 不传默认是空格

justs = 'apple'
print(justs.ljust(10,"*")) # 向右填充字符串 满足一共10个字符
print(justs.rjust(10,"%")) # 向左填充字符串 满足一共10个字符


print (name.count('i'))  # 字符串中 某个字符的个数
print (name.count('i',6))  # 从某一个位置开始找
print (name.count('i',1,7)) # 起始位置 结束位置

print (name.endswith('g'))  # 是否以什么结尾的
print (name.endswith('g',4,5)) # 起始位置 结束位置

print (name.startswith('x',3)) # 是否以什么开头  ---  开始和末端

# 将tab符号改为空格生成新的字符串
tabs = "1234567\t9"
print (tabs.expandtabs(6))  # 6-1 空格数  每6个为一组找到 \t
print (len(tabs.expandtabs(6)))

finds = "nihaoxiaoming"
print (finds.find('x'))  # 从前往后找 出现的第一个位置
print (finds.find('i',2,10)) # 在一个区间内去查找

indexs = "helloe"
print(indexs.index('e'))  # 同find



fomats = "i am {name} ,age is {age}"
fomats1 = "i  like {0} and {1}"
res1 = fomats1.format('apple','juce')  # 数字占位
res = fomats.format(name='lihua', age='30')   # 字符串格式化
print (res,res1)

res3 = fomats.format_map({"name":"lili", "age":"30"})
print  (res3)




# 字符串格式化
msg = 'i am %s age is %d' % ('lili',30)  # i am lili age is 30  百分号后边的数据可以是任意类型（如果是%s）  也可以放变量

# %d 是数值
print(msg)

floats = 'floats is %f' % (22.111324934242)  # 默认保留的是六位小数,会做四舍五入计算
floats1 = 'floats is %.2f' % (22.111324934242) # 保留两位小数
print(floats,floats1)

# 打印百分比
floatsx = 'percent is %.2f %%' % (22.111324934242)
print(floatsx)  #percent is 22.11 %

# 即使传入的数字也会当字符串操作
strm = '字符串截取操作 %.3s  数字截取 %.4s' % ('hello',99.1234966)  # 截取前三个字符  字符串截取操作 hel  数字截取 99.1
print(strm)

# 键值传值 %()s
strms_ = 'i am %(name)s' % {"name": "aihua"}
print(strms_)

# 分隔符
print('name','lili','age',20,sep=':') # name:lili:age:20



alnums = "nidadai12223"
print(alnums.isalnum())   # 判断字符串中是否只有字符串或者数字

alphas = "aaaa你好"
print(alphas.isalpha())   # 判断是否只有 字母或 汉字

decimal = "1111111"
print(decimal.isdecimal())  # 判断是否只有数字
print(decimal.isdigit())   # 同上  特殊字符的数字 可以识别
numer = "1111"
print(numer.isnumeric()) # 判断是否是数字  中文也支持


identifal = "_sdad9988sadef"
print(identifal.isidentifier())  # 数字字母下划线


prints = "sssss&nbsp;sss\n"
print(prints.isprintable())  # 判断是否有不可见的字符

space = "   "
print(space.isspace())  # 判断是否是空字符串

title = "kkk sda sa sa swqq"
print(title.title())  # 标题  单词首字母大写
print(title.istitle()) # 判断是否是标题


joins = "你好啊"
print(' '.join(joins))  # 添加指定分隔符


strip = "s sda sda sa "
print(strip.lstrip()) # 去除左边空格   也可以去除换行 \n \t
print(strip.rstrip()) # 去除右边空格  同上
print(strip.strip()) # 去除左右空格  同上

print(strip.lstrip('s'))  # 去除指定字符的最大限度的序列 ++++ 没有则不去除



translates = "春眠不觉晓"
ofs = str.maketrans('春眠不觉晓','处处蚊子咬')  # 对应替换
resl = translates.translate(ofs)
print(resl)


pre = "sdadadadsfada"
print(pre.partition('a'))  # 以a为分割 分成三份  ('sd', 'a', 'dadadsfada')
print(pre.rpartition('a')) # ('sdadadadsfad', 'a', '')

print(pre.split('a')) # 分割 ['sd', 'd', 'd', 'dsf', 'd', '']  参数消失
print(pre.split('a',2)) # ['sd', 'd', 'dadsfada']  只分2次 参数消失2次
print(pre.rsplit('a'))

splines = "sdada\nsda\nsda"
print(splines.splitlines(True))  # 是否保留换行符分割 ['sdada\n', 'sda\n', 'sda']



var1 = "abca"
print(var1[0])  # 索引取值
print(var1[0:1]) # a  0=< <1   切片

print(len(var1))  # 判断个数  也可以是判断列表个数

print(var1.replace('a','n',1)) # 字符串替换 , 替换几个

for t in var1 :
    print(t)

v = range(0,10)  # 省内存 连续存数

for item in v :
    print(item)    # 0 - 9

v1 = range(0,20,5)   # 0 5 10 15 ... 15
for item in v1 :
    print(item)

# inpu_ = input(">>>>>>>")
#
# for item in range(0,len(inpu_)) :
#     print(item, inpu_[item])










