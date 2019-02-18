# -*- coding: UTF-8 -*- 
def test () :
    yield  1
    yield  2
    yield  3    # 可以作为return返回   主要作用保留函数的运行状态   yield可以多次执行  return只能一次

# 生成器对象基于迭代器   自动实现迭代器协议

res = test()
print(res)   # <generator object test at 0x103592408>  生成器对象
print(res.__next__())  # 1
print(res.__next__())  # 2
print(res.__next__())  # 3

# 补充： time.sleep(3)  表示隔三秒执行


# 读取文件中的人口数
def get_people() :
    with open('people','r',encoding='utf-8') as f :
        for i in f:
            yield  i

g = get_people()
# print(g.__next__()) # {"江苏": "10000w"}  返回实际上是字符串
# print(g.__next__()) #  {"河南": "20000w"}
#
# # 拿到结果
# print(eval(g.__next__())['num'])  # 将字符串转成字典类型
#
# for i in g:    # 实际上执行的也是next方法  会打印剩下的人口数
#     p_dic = eval(i)
#     nu = p_dic['num']
#    # print(nu.rstrip('w'))


# 重点： 迭代只能一次 不然 后边不好处理
# 如果上边也有for循环或者next方法 下边执行的时候不是从头开始
# 生成器取和
sums = sum(eval(i)['num'] for i in g)
print(sums)  # 374690

import  time
# 生产消费者模型  单线程处理并发


# 消费者
def consumer (name) :
    print('i am [%s],哈哈哈' % name)
    while True:
        yous = yield
        time.sleep(1)
        print('%s 哈哈哈哈 你是 [%s]' % (name,yous))
# 生产者
def producer(name) :

    cl = consumer(name)
    # 可以定义多个消费者 c2,c3,c4...
    cl.__next__()

    for i in range(10) :
        time.sleep(1)
        cl.send(i)   # send 方法  lili
    # cl.__next__()  # none
    # cl.send('ooo')  # ooo

producer('xiaojun')