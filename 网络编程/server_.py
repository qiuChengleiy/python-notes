# -*- coding: UTF-8 -*- 
import  socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 套接字，TCP协议---基于流式 -- 建立socket对象 -- IPv4
phone.bind(('127.0.0.1',8000))  # 绑定端口 绑定IP地址

phone.listen(5) # 最多有5个连接在等待 ---  backlog

#关于5的解答：

# 这个参数指定是**等待队列**的长度。
#
# 也就是如果系统可以并发处理100个请求，同时到达106个请求，100个请求直接被处理，5个等待，第106个直接就拒绝。
#
# 上万个请求进来，系统不是每次接受5个用户，而是可以让5个用户等待，系统每次接受的用户取决于系统吞吐量。
#
# 而且一般应用传5就够了，一万个并发的应用显然也不是一般应用了

print('正在等待连接------')
conn,addr = phone.accept()  # 拿到 连接和地址  --- 这个过程它会一直等---直到拿到连接它才会执行下边的代码

msg = conn.recv(1024) # 允许接收的字节长度

print('msg---->',msg)

conn.send(msg.upper())  # 发送消息

conn.close()  # 关闭连接
phone.close()  # 关闭socket 关闭程序
