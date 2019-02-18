# -*- coding: UTF-8 -*-

# 函数定义
def funcs (name) :
    print(name)

funcs('lili')


# 匿名函数
nick = lambda name:name+'1'   # 后边只能是表达式  不能以复杂的逻辑   参数可以是多个 x,yz:....
print(nick('aihua'))  # aihua1


# 高阶函数  即： 函数作为参数进行传递

def bar(name) :
    return name

def far(name) :
    return name

res = far(bar)
print(res) # <function bar at 0x10e3e4ea0>  返回bar的内存地址    返回值可以是函数
res1 = far(bar('xiaoming'))
print(res1)  # 将函数执行的结果传递进去

def bars (name,age) :
    return name(age)   # 尾调用优化

res2 = bars(far,'20')
print(res2)


# 内置map  1.函数名  2.可迭代对象
list1 = [1,2,3,4]
results = map(lambda x:x+1,list1)
print(list(results)) # [2, 3, 4, 5]

# filter 过滤函数
list2 = [1,2,3,4,5]
def fu1(num) :
    return num % 2 == 0

results1 = filter(fu1, list2)
print(list(results1))

# reduce  将第一个元素与第二个元素运算，得到的结果再和第三个元素运算
from functools import  reduce
def redu (x,y) :
    return x+y

result2 = reduce(redu,[1,2,3,4])
print(result2)  # 10

# 其它内置函数
print(abs(-1))   # 绝对值
print(all([1,2,3,4,0]))  # 判断是否全为真值  也可以传字符串 0假 1真
print(any(['',1]))  # 判断是否有一个真

print(bin(2))  # 转二进制
print(bool(1)) # 布尔转换

print(hex(22)) # 10进制转16进制
print(oct(12)) # 10进制转8进制

# gbk uft8可以编中文码   ascill不可以编码中文
print(bytes('你好',encoding='utf-8'))  # b'\xe4\xbd\xa0\xe5\xa5\xbd' 二进制  字节 将字符串编码   内存的是unicode编码
print(bytes('你好',encoding='utf-8').decode('utf-8')) # 解码


# chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。  acill码对应的字母
print(chr(0x30), chr(0x31), chr(0x61))   # 0 1 a

# asiall码对应的位置 数字
print(ord('a'))


# 取商数取余数
print(divmod(10,3))  #(3, 1)  10除以3

dics = '{"k1":"dididi"}'
print(eval(dics))   # 将字符串中的数据结构提出来
add = '10+10'
print(eval(add))   # 可以将字符串的数学运算进行计算

print(globals())  # 返回全局变量
print(locals()) # 局部变量 主要： 运行作用域不同会结果会不同

# hash:  可hash的都是不可变类型数据  都会得到一个固定的值 而且值不同  不可以反推传进去的参数
print(hash('sdadasdasdsfsaifao'))

print(dir(str))   # 返回方法名

# print(help(str)) # 返回帮助信息

# 对象判断
print(isinstance(1,int))
# print(issubclass())  super类 --- 派生类

lisp = [1,2,3,-5]
dico = {"k1": 1,"k2":2,"k3":0}
print(max(lisp))  # 最大值
print(min(lisp))  # 最小值

# min 同 max

print(max(dico.values()))  # 取字典的最大值
print(max(dico))  # 会比较key  字符串的话一个一个比较  比如 vvva111 < vvva2  字母之间也有大小比较  不同类型间不能比较

# 取出字典中最大的值和对应的Key
print(max(list(zip(dico.values(),dico.keys()))))  # (2, 'k2')


#zip拉链  传进去的要是序列  转成一一对应的元组  如果左边或者右边长的 则舍掉剩下的
print(list(zip((1,2,3),('ni','hao','a'))))  # [(1, 'ni'), (2, 'hao'), (3, 'a')]

dicsp = {"k":"v","k1":"v1"}
print(list(zip(dicsp.keys(),dicsp.values())))  # [('k', 'v'), ('k1', 'v1')]

print(list(zip([1,2,3,4],'nihaoa'))) # [(1, 'n'), (2, 'i'), (3, 'h'), (4, 'a')]


print(pow(2,3)) # 2的三次方 相当于2**3
print(pow(2,3,5))  # 相当于2**3%5 取余数


print(round(2.1))  #四舍五入

s = 'hello'
print(s[slice(3,5)])  # 切片 s[3:5]
print(s[slice(1,4,2)]) # 步长2  每隔2取一个  ---- el


# sorted 排序 不同类型之间不能排序
p_list = [
    {"name": "lili","age": 20},
    {"name": "xiaohua", "age": 30},
    {"name": "xiaoli", "age": 10},
    {"name": "xiaohong", "age": 60},
    {"name": "xiaohui", "age": 40},
]

# 按照年龄排序
print(sorted(p_list,key= lambda dic:dic['age']))
# [{'name': 'xiaoli', 'age': 10}, {'name': 'lili', 'age': 20}, {'name': 'xiaohua', 'age': 30}, {'name': 'xiaohui', 'age': 40}, {'name': 'xiaohong', 'age': 60}]

class_dic = {
    "name1": 20,
    "name2": 30,
    "name3": 10,
    "name4": 80,
}

# 单独的字典排序
print(sorted(class_dic,key= lambda key:class_dic[key])) # ['name3', 'name1', 'name2', 'name4']
# 并拿到对应的值
print(sorted(zip(class_dic.values(),class_dic.keys()))) # [(10, 'name3'), (20, 'name1'), (30, 'name2'), (80, 'name4')]



# 模块调用  import 不能导入字符串   __import__(module_name) 可以导入字符串名
from func import tests
tests.hellos('world')   # helloworld


