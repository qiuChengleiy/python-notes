# -*- coding: UTF-8 -*- 
# 时间模块

import time

# 延迟进程
# time.sleep(1)
print('year')

# 时间戳
print(time.time())  # 1546596349.622891秒

# 结构化时间  本地时间对象  tm_yday 表示1月1到今天过了多少天了
print(time.localtime()) #ime.struct_time(tm_year=2019, tm_mon=1, tm_mday=4, tm_hour=18, tm_min=7, tm_sec=41, tm_wday=4, tm_yday=4, tm_isdst=0)
print(time.localtime().tm_year)  # 2019年

#另一种的时间结构对象  另一个时区（英国） UTC时间标准时间
print(time.gmtime()) # time.struct_time(tm_year=2019, tm_mon=1, tm_mday=4, tm_hour=10, tm_min=12, tm_sec=53, tm_wday=4, tm_yday=4, tm_isdst=0)


# 将一个结构化时间转换成时间戳
t = time.localtime()
print(time.mktime(t))


# 将结构化时间转换成字符串形式
print(time.strftime("%Y-%m-%d %X",time.localtime()))  # 2019-01-04 18:24:38

# 将字符串时间转化成结构化时间
print(time.strptime("2016:12:12 12:30:45","%Y:%m:%d %X")) #time.struct_time(tm_year=2016, tm_mon=12, tm_mday=12, tm_hour=12, tm_min=30, tm_sec=45, tm_wday=0, tm_yday=347, tm_isdst=-1)

# 直接打印出直观的时间
print(time.asctime()) # Fri Jan  4 18:33:06 2019
print(time.ctime()) # Fri Jan  4 18:35:05 2019


# datetime
import  datetime
print(datetime.datetime.now())  # 2019-01-04 18:39:04.270337







