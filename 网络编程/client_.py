# -*- coding: UTF-8 -*-
import  socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 基于流式
phone.connect(('127.0.0.1',8000))  # 建立连接

# 循环发送
while True:
    phone.send('hello'.encode('utf-8'))  # 发消息 字节 ---- 二进制
                                                # 发送空消息 服务端卡住
    # 原因在于发往空到内核态缓存，在取的时候自然取不到，即无法发消息
    # 收发消息跟自己一端的（服务端或客户端）缓存有关


    data = phone.recv(1024)  # 收消息

    print('收到服务端',data)

phone.close()

# 强行关闭客户端 会导致服务端也会爆粗 原因在于 关闭后 conn挂掉 recv没有意义
# 这样的服务端只能服务一个人
# 解决办法 --- 循环接收请求