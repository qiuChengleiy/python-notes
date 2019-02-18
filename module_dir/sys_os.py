# -*- coding: UTF-8 -*-
# 系统模块
import os,sys

print(__file__)  # /Users/qiuchenglei/python/module_dir/sys_os.py

# 临时环境变量
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
# print(sys.path)
# ['/Users/qiuchenglei/python/module_dir', '/Users/qiuchenglei/python', '/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7/lib/python37.zip', '/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7/lib/python3.7', '/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload', '/usr/local/lib/python3.7/site-packages', '/Applications/PyCharm.app/Contents/helpers/pycharm_matplotlib_backend', '/Users/qiuchenglei/python']

# 工作目录
print(os.getcwd())  # /Users/qiuchenglei/python/module_dir

os.chdir('test')  # 进入test目录
print(os.getcwd()) # /Users/qiuchenglei/python/module_dir/test

print(os.curdir)  # .
print(os.pardir) # ..

# os.makedirs('mkdirs/mkd')  # 生成多层递归目录  test/mkdirs/mkd


os.chdir('../')
print(os.getcwd())
# os.makedirs('mkdirs/mkd')  # 创建和删除同时执行时 只会创建
# os.removedirs('mkdirs/mkd') # 只删除空目录--删除相应目录 如果为空则删除目录 如果它的递归 --父级目录为空---则--删除--父级目录

# 单一目录操作
# os.mkdir('hello') # 创建目录
# os.rmdir('hello') # 只删除空目录


# 列出当前目录下文件夹以及文件
# print(os.listdir())
# ['randows.py', 'test', '__pycache__', 'test.py', 'times.py', 'imports.py', 'modules', 'sys_os.py']


# os.remove('rem')  删除一个文件操作


#  列出文件信息
print(os.stat('test.py'))
# size 字节   st_atime上次用户访问时间    st_mtime 上次用户修改时间   st_ctime 用户创建时间

# 路劲分隔符
print(os.sep) # /    win: \

# 换行符
print(os.linesep) # \n    win: \r\n

#文件路劲分隔符
print(os.pathsep) # :   win: ;

# 系统名字
print(os.name)  # posix  win: nt

# 运行shell 命令  运行终端命令
# os.system('open ./')

# 系统环境变量
# print(os.environ)

# 返回绝对路劲
print(os.path.abspath('test')) # /Users/qiuchenglei/python/module_dir/test

# 分割路径成元组
print(os.path.split('test/mkdirs')) # ('test', 'mkdirs')

# 返回上一次
print(os.path.dirname('test/mkdirs')) # test

# 返回最后一个名字
print(os.path.basename('test/mkdirs')) # mkdirs


# 判断路径是否存在
print(os.path.exists('test'))  # True

# 判断是否是绝对路径
print(os.path.isabs('test'))  # False

# 判断是否存在文件
print(os.path.isfile('test'))  # False

#目录是否存在
print(os.path.isdir('test')) #True


# 路径拼接
print(os.path.join('test','dirs','abc'))  # test/dirs/abc

print(os.path.getatime('test'))  # 返回目录或文件最后存取时间
print(os.path.getmtime('test'))  # 返回目录或文件最后修改时间


# 返回模块的搜索路径
print(sys.path)

# sys.exit(0) # 0 正常退出程序
print("已经终止了")

# 返回py版本信息
print(sys.version) # 3.7.0 (default, Jun 29 2018, 20:13:13)

# 返回平台信息
print(sys.platform) #darwin

# 获取终端输入的信息
print(sys.argv) # ['/Users/qiuchenglei/python/module_dir/sys_os.py'] 默认信息

# 模拟终端进度条
import time
for i in range(10):
    sys.stdout.write('\033[1;32;40m%s' % '#')  # 向终端写入   颜色代码  格式：\033[显示方式;前景色;背景色m  pycharm显示不一样
    time.sleep(0.1)
    sys.stdout.flush() # 刷新缓存
print('\n')







