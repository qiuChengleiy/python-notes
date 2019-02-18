# -*- coding: UTF-8 -*- 
# import test
#print(test)  # 会运行完所有的代码 相当于加载代码块
# 也可以这么导入
# from module_dir.test import adds   # 导入具体的函数了

# 引入外部文件夹内的包
from module_dir.modules import cal

# 导入所有函数
from module_dir.modules.cal import *  # 相当于把所有的函数都导入 可以直接使用

# 注意：模块的方法名带有 _开头的是不能被导入的


print(__name__)  # __main__   表示主文件  不被别人文件调用

if __name__ == '__main__':
    print('我来执行我写的功能')

# package  自带init.py
# 当import一个package就会自动执行初始化函数


# 动态模块导入 --- 不管嵌套多少始终是最顶层
m1 = __import__('modules.cal')   # 通过字符串的方式
print(m1)  # <module 'modules' (namespace)>
m1.cal.adds()  # 需要这样调用


# 利用解释器自己的
import importlib   # 底层是基于反射来做的
m = importlib.import_module('modules.cal') # 可以直接定位到具体的
print(m) # <module 'modules.cal' from '/Users/qiuchenglei/python/module_dir/modules/cal.py'>


# 避免换平台后模块导入失效 （pycharm会帮助加入环境变量）
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# 模块倒入
#from...




