# -*- coding: UTF-8 -*- 
# 错误分为语法和异常 -- 语法错误与异常处理无关
# 异常处理是为了防止程序崩溃
# if elif else 处理异常  --- 异常逻辑处理   不推荐 - 可能导致大量的if 可读性差

# try except 在无法预知的异常情况下使用 --- 无脑使用只会导致程序繁琐 可读性变差

# try 异常处理
try:
    age = input('>>>')
    print(int(age))

    age1 = input('>>>')   # 因为上边触发了异常所以这里不会被执行 --- 如果没有异常照常执行
    print(int(age1))

except ValueError as e:   # except 错误类型   --- ValueError只能处理指定的异常
    print(e)   # invalid literal for int() with base 10: 'sdadad'
except KeyError as e:  # ---- except可以多分支处理
    print(e)

print('异常被捕捉到了')  # 不影响后续代码的执行


# ---- 万能异常
try:
    age = input('>>>')
    print(int(age))

    age1 = input('>>>')   # 因为上边触发了异常所以这里不会被执行 --- 如果没有异常照常执行
    print(int(age1))

except Exception as e:   # 万能异常类 --- Exception
    print(e)


# 逻辑处理
try:
    age = input('>>>')
    print(int(age))

    age1 = input('>>>')   # 因为上边触发了异常所以这里不会被执行 --- 如果没有异常照常执行
    print(int(age1))

except Exception as e:   # 万能异常类 --- Exception
    print(e)
else:
    print('try代码块里没有异常,我开始执行')
finally:
    print('不管你是不是有异常，我还是照常执行')


# ---- 主动触发异常
try:
   raise TypeError('类型错误')  # ---- raise
except Exception as e:   # 万能异常类 --- Exception
    print(e)














