# -*- coding: UTF-8 -*-
# logging 模块
import logging

# 级别
# logging.debug('debug message')
# logging.info()
# logging.warning()    默认是 warning级别
# logging.error()
# logging.critical()

# 级别配置  ---- 通过函数配置
# logging.basicConfig(
#     level=logging.DEBUG,   # 把级别调到DEBUG
#     filename= 'loger.log',  # 把信息写入日志文件
#     filemode= 'w',   # 重写文件  如果 不写的话 就是追加日志
#     # 日志格式   message就是写入的信息  filename 文件名  lineno行号 --- 时间   默认是debug,info....
#     # 除了filename 还有其他的参数 -- 参考博客
#     format= '%(asctime)s %(filename)s [%(lineno)d]  %(message)s',
#
# )
#
# logging.debug('设置好的等级')
# logging.info('info')
# logging.info('info4')




# 通过logger对象
# 封装到一个函数
def logger() :
    logger = logging.getLogger()  # 这是一个用户 root 根用户  树状结构
    # logger2 = logging.getLogger('mylog')  可以设置多个子用户 设置不同级别 打印不同信息
    # name值相同时  赋值给不同变量时   级别依然相同
    # 子用户的子用户 name.son_name
    # 根用户和子用户在执行时 跟用户只会执行自己的  子用户如果发现根用户也在执行时（创建即视为执行）它会顺便把根用户的也会打印一次


    fh = logging.FileHandler('loging.log')  # 向文件发送
    ch = logging.StreamHandler() # 向终端发送

    # 创建格式
    fm = logging.Formatter('%(asctime)s %(filename)s [%(lineno)d]  %(message)s')

    # 使用格式
    fh.setFormatter(fm)
    ch.setFormatter(fm)

    # 加入最终对象
    logger.addHandler(fh)
    logger.addHandler(ch)

    # 设定级别
    logger.setLevel('DEBUG')

    return logger

logger = logger()
# 打印日志信息  ---  终端+日志文件
logger.debug('hello deubg')
logger.info('info')
logger.warning('warn')
logger.error('error')
logger.critical('critical')








