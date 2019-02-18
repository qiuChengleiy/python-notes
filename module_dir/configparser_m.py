# -*- coding: UTF-8 -*- 
# configparser 模块  -----  配置文件解析
import configparser

# 配置文件格式
# [DEFAULT]
#
# [..]
#
# [..]


# 生成配置文件

config = configparser.ConfigParser()

# 配置键值对
# config['DEFAULT'] = {
#     "K1": 1,
#     "K2": 2,
#     "K3": 3,
#     "K4": 4,
# }
#
# # 写入文件  文件的配置扩展名随意 --- 建议 ini
# with open('configs_n.ini','w') as configfile:
#     config.write(configfile)


# 操作 ----  增删改查

config.read('configs_n.ini')   # 读取配置文件
print(config.sections())   # 获取除default以外的   []块名

# 判断 块是否在里面
print('test.org' in config.sections())  # True

# 取值  ---  【】不区分大小写
print(config['DEFAULT']['k1']) # 1

# 遍历某个块下边的值  如果有DEFAULT配置 都会打印出来  有重复则不会重复打印
for i in config['test.org']:
    print(i)  # k1,k2,k3,k4，defaults


# 相当于遍历  ---- 有default
print(config.options('test.org')) # ['k1', 'k2', 'k3', 'k4', 'defaults']

# 会拿到下边的键值   ---- 有default
print(config.items('test.org')) # [('k1', '1'), ('k2', '2'), ('k3', '3'), ('k4', '4'), ('defaults', "'我是任何遍历的时候都会出来的'")]

# 拿到对应的值   ---- 有default
print(config.get('test.org','defaults'))



# 增加 块
config.add_section('add_sec')

# 添加配置
# config['add_sec'] = {
#     "add": 1,
#     "add1": 2,
#     "add2": 3,
#     "add3": 4,
# }

# 也可以这样加
config.set('add_sec','add_set','yes')


# 删除 块
config.remove_section('test.org')

# 删除某个块下的键值对
config.remove_option('add_sec','add_set')


# 将修改后的配置写到新的文件里
config.write(open('new_config.ini','w'))
