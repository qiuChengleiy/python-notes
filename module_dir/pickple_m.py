# -*- coding: UTF-8 -*- 
# pickle模块
import pickle

# pickle 支持的数据类型比较多 可以是函数 类


dic = {'name': 'lili'}

data = pickle.dumps(dic)  #转成序列化 如果写入文件里是看不懂的  写入的话只能是wb模式 而json写入文件是可读的（打开看的懂）

print(data,type(data))  # 类型是字节
# b'\x80\x03}q\x00X\x04\x00\x00\x00nameq\x01X\x04\x00\x00\x00liliq\x02s.' <class 'bytes'>

print(pickle.loads(data)) # {'name': 'lili'}


# load 和 dump 同 json

