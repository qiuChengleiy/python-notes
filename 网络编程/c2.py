# -*- coding: UTF-8 -*- 
# 第二个链接
import  socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 基于流式
phone.connect(('127.0.0.1',8000))  # 建立连接

phone.send('c2c2c2c2c2c2'.encode('utf-8'))  # 发消息 字节 ---- 二进制


data = phone.recv(1024)  # 收消息

print('收到服务端', data)

phone.close()

# 强行关闭客户端 会导致服务端也会爆粗 原因在于 关闭后 conn挂掉 recv没有意义
# 这样的服务端只能服务一个人
# 解决办法 --- 循环接收请求