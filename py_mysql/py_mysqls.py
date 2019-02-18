# -*- coding: UTF-8 -*- 
# python 操作数据库
import pymysql

# 连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='admin',
    passwd='yourpass',
    db='test1'
)

# 游标
cursor = conn.cursor()

# 执行sql
sql = 'select * from stud'
row = cursor.execute(sql)


# 获取
print(row)  # 返回几条结果

one = cursor.fetchone()   # 拿一条结果
print(one)

two = cursor.fetchmany(2)   # 拿2条记录
print(two)

# --- 实际上游标已经移到了上边记录的后边
all = cursor.fetchall()  # 拿到所有记录  --- 如果前面有fetch操作的话 只会拿剩下的
print(all)


# --- 游标移到
cursor.scroll(2,mode='absolute')   # -- 绝对定位
print(cursor.fetchone())   # --- 再取的时候已经在第三位置了 --- 位置相当于走了一个单位



cursor.scroll(-1,mode='relative')   # -- 相对定位
print(cursor.fetchone())   # --- 再取的时候已经在第三位置了
