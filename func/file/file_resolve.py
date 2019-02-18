# -*- coding: UTF-8 -*- 
f = open('test.py','rb')  # b模式不能指定编码
# 读操作
data = f.read()
print(data)   # b'# -*- coding: UTF-8 -*- \naaaaa\nbbb\nccc\n111\n\xe4\xbd\xa0\xe5\xa5\xbd\xe5\x95\x8a\xe4\xb8\x96\xe7\x95\x8c\n\n\n'

# 读取内容  二进制转字符串
print(data.decode())

f.close()  # 关闭
# aaaaa
# bbb
# ccc
# 111
# 你好啊世界

f1 = open('test.py','wb')  # wb写模式
f2 = open('test.py','ab')  # ab接着下一行写
# 写操作  需要编码
f1.write(bytes('嗯 很好啊\n',encoding='utf-8'))  # 将文件全部重写  也可以是 'en'.encode()
f2.write(bytes('嗯 很好啊 行\n',encoding='utf-8'))
f1.close()
f2.close()
# 其他方法
print(f1.closed)  # 判断是否关闭



f3 = open('a.txt','w+',encoding='utf-8')  # 如果文件不存在 自动创建   不知道编码的时候可以以 'latin-1' 的编码方式 encoding = 'latin-1'
print(f3.encoding)  # UTF-8   返回以什么编码方式打开的

f3.write('数据都在内存里，必须刷新才能保存到硬盘')
f3.flush()  # 保存

print(f3.name)  # 文件名

print(f3.tell()) # 57

# f3.readline()  读取一行  光标换行
# f3.readlines()  读取所有数据放到列表中

# f3.seek(1)  # 光标在1后边的位置

#f3.read(1) # 读取一个字符

# f3.truncate(10) # 截取开头到第10个位置















