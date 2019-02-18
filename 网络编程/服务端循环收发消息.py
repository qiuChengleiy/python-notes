# -*- coding: UTF-8 -*-
import  socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 套接字，TCP协议---基于流式 -- 建立socket对象 -- IPv4
phone.bind(('127.0.0.1',8000))  # 绑定端口 绑定IP地址

phone.listen(5) # 最多有5个连接在等待 ---  backlog

print('正在等待连接------')
# 循环请求
while True:
    conn,addr = phone.accept()  # 拿到 连接和客户端地址  --- 这个过程它会一直等---直到拿到连接它才会执行下边的代码
    # 循环任务
    while True:
       try:    # try 捕捉可能异常断开的连接
        msg = conn.recv(1024) # 允许接收的字节长度
        if  msg.decode() == '':
            break  # 关闭连接
        print('msg---->',msg)
        conn.send(msg.upper())  # 发送消息
       except Exception:
           break
    conn.close()  # 关闭连接


phone.close()  # 关闭socket 关闭程序




# 强行关闭客户端 会导致服务端也会报错 原因在于 关闭后 conn挂掉 recv没有意义
# 这样的服务端只能服务一个人
# 解决办法 --- 循环接收请求







