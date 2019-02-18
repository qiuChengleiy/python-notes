# -*- coding: UTF-8 -*- 
# 装饰器特点：
# 1. 本质即函数
# 2. 为其他函数添加新功能

# 原则
# 1. 不修改被修饰函数的源代码
# 2. 不修改被修饰函数的调用方式

# 装饰器 = 高阶函数 + 函数嵌套 + 闭包
# 闭包： 函数体对外部函数作用域的变量引用

import  time

def cal():
    t = 0
    start_t = time.time()
    for i in range(10):
        t+=i
        time.sleep(1)
        stop_t = time.time()

    return '结果是 %d 运行时间是 %d' % (t, stop_t - start_t)

# print(cal())


# 装饰器骨架

def timer(func):  # 为函数添加运行时间的功能
    def wrapper(*args,**kwargs):   # 解决传参问题 *args **kwargs  获取传入的所有参数
        start_time = time.time()
        # func()
        # 如果函数时带返回值的
        res = func(*args,**kwargs)   # 接收参数
        stop_time = time.time()
        print('函数运行时间是 %s' % (stop_time-start_time))
        return res
    return wrapper


# 测试函数
# 语法糖   @timer就相当于  test = timer(test)
@timer
def test(name,age):
    time.sleep(3)
    print('运行完毕 %s , %s' % (name,age))
    return '我是返回值哦'

# 需要赋值操作
# res = timer(test)
# res()

# 经过装饰器直接调用test  ---- 不改变源代码  不改变调用方式
print(test('lili',30))  # 可以拿到返回值 并且能打印出参数 ---- 运行完毕 lili , 30


