# -*- coding: UTF-8 -*- 

f = open('b.txt','rb')
print(f.tell())  # 读取光标的位置 0
# f.seek(10) # 移动光标
# print(f.tell())  # 10
# f.seek(3)
# print(f.tell()) # 3     默认是从开头算的
#
# f.seek(4,1)  # 相对上边3的位置 移动4个 得到7   =======   1
# print(f.tell()) # 7

f.seek(-8,2)  # 倒着读   倒着8个字符
print(f.tell())  # 10

data = f.read()   #从第10个字符读取 剩下的字符
print(data.decode())  # o 你好    每一行结尾 \r\n
f.close()


# 读文件最后一行    小文件
f1 = open('log','rb')
# data = f1.readlines()
# print(data[-1].decode('utf-8'))

print(f1.tell())
# 循环文件的方式  要一行给一行
# for i in f1 :
#     print(i)

# seek 读取最后一行
for i in f1 :
    offs = -2
    while True:
        f1.seek(offs, 2)
       # print(f1.tell())
        data = f1.readlines()
       # print(data)
        if len(data) > 1 :
            print(data[-1].decode('utf-8'))
            break
        offs*=2