# -*- coding: UTF-8 -*- 
class A:
    def __init__(self,name):
        self.name = name

    def __enter__(self):   # 先触发
        print('enter')  # enter
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # 最后触发 --- 异常也会触发
        print('exit')  # exit
        return  True   # ---- 有异常 照常继续执行后续代码

# with 触发 enter  返回的值赋值给 a
with A('lili') as a :
    print(a)  # <__main__.A object at 0x10c3a7f98>
    print('11111')
    print('222222')

















