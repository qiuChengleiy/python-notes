# -*- coding: UTF-8 -*- 
# 基于TCPsocket的HTTP服务器:
#
# 上面的例子中，我们已经可以使用TCP socket来为两台远程计算机建立连接。然而，socket传输自由度太高，从而带来很多安全和兼容的问题。我们往往利用一些应用层的协议(比如HTTP协议)
# 来规定socket使用规则，以及所传输信息的格式。
#
# HTTP协议利用请求 - 回应(request - response)
# 的方式来使用TCP
# socket。客户端向服务器发一段文本作为request，服务器端在接收到request之后，向客户端发送一段文本作为response。在完成了这样一次request - response交易之后，TCP
# socket被废弃。下次的request将建立新的socket。request和response本质上说是两个文本，只是HTTP协议对这两个文本都有一定的格式要求。


import socket

HOST = ''
PORT = 8002

text_content = '''
HTTP/1.1 200 OK  
Content-Type: text/html

<head>
<title>基于tcp的http服务</title>
</head>
<html>
<p>Wow, Python Server</p>
<IMG src="socket.png"/>
</html>
'''

# 文件读写 --- 可以创建一个web静态资源服务器
f = open('socket.png','rb')
pic_content = '''
HTTP/1.1 200 OK  
Content-Type: image/jpg

'''
pic_content = pic_content.encode() + f.read()
f.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

while True:
    s.listen(3)
    conn, addr = s.accept()
    request = conn.recv(1024)
    method = request.decode().split(' ')[0]
    src = request.decode().split(' ')[1]

    if method == 'GET':
        if src == '/socket.png':
            content = pic_content
        else:
            content = text_content.encode()

        print('Connected by', addr)
        print('Request is:', request)
        conn.sendall(bytes(content))   # 必须以字节的形式发送

    conn.close()
















