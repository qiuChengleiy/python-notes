# -*- coding: UTF-8 -*- 
# requests 请求库 模块详解 ----

# 安装：pip3 install requests

import  requests
from bs4 import BeautifulSoup

# 相当于做了一个网页下载
res = requests.get(
    url='http://www.autohome.com.cn/news/'
)

res.encoding = res.apparent_encoding  # 设置字符编码

soup = BeautifulSoup(res.text, features='html.parser')    # 解析

target = soup.find(id='auto-channel-lazyload-article') # 找到目标节点 --- html的 id 标签

obj = target.find('li')  # 找到目标节点下的 一个li节点 --- 1个

obj_li = target.find_all('li') # 找到所有

for i in obj_li:
    a = i.find('a')  # 拿到li下的 a标签
    if a:
       # print('http:%s' % (a.attrs.get('href')))
   # print(a.attrs)  # 拿到a标签的属性 ---- 属性存着连接  {'href': '//www.autohome.com.cn/news/201901/928690.html#pvareaid=102624'}
        text = a.find('h3').text
        # print('%s\n' % text,'http:%s' % (a.attrs.get('href')))

        # 图片下载：
        img_src ='http:%s' % a.find('img').attrs['src']  # 先拿到连接
        res_img = requests.get(url=img_src)  # 拿到对应图片资源
        import uuid
        file_name = './img/%s' % str(uuid.uuid4()) + '.jpg'
        # 写入文件
        with open(file_name, 'wb') as f:
             f.write(res_img.content)

        print(img_src)

# print(obj_li)

















