# -*- coding: UTF-8 -*- 
# 字典
dic = {             # 字典的value可以是任意数据类型  key不能是列表,字典    +++++可以是元组++++
    "k1": "111",
    "k2": {
      "k3": "sss",
      "k4": True,
    },
    "k5": (1,2,3,4),
    1: "nihao",
    (1,3): False,
}

print(dic) # 字典是无序的  当键值重复时 只能存一个 会覆盖之前的

print(dic.keys(),dic.values(),dic.items()) # 得到keys  values  key+value 列表

print(dic['k5'])  # 键值取值

for k,v in dic.items() :   # 字典循环
    print(k, v)

ddc = {"k1":"1"}
ddc.clear()  # 清空
print(ddc)
ddc.copy()  # 浅拷贝
print(ddc)

new_dic = dict.fromkeys(["k1","k2","k3"],"hello")  # 生成字典
print(new_dic)  # {'k1': 'hello', 'k2': 'hello', 'k3': 'hello'}


v = ddc.get("k1","我自己生成的")  # 取值  如果键名不存在 传默认值
print(v,ddc) # 我自己生成的 {}  此时字典并不会改变

dic1 = {"k1":"111","k2":"2222","k3":"444",}
vm = dic1.pop("k1",90)  # {'k2': '2222', 'k3': '444'} 111  删除k1 并反回对应的值
vm_ = dic1.pop("kkkk","传个默认值")  # 如果删除的key值不存在 则返回默认值
print(dic1,vm,vm_)

pop_item = dic1.popitem()   # 随机删除一个
k,v = dic1.popitem()  # 获取随机删掉的 k v
print(pop_item,dic1,k,v) # ('k3', '444')

dicz = {"k1": "nihao"}
dicz["k1"] = 111   # 可以直接修改
print(dicz)

ress = dicz.setdefault('k1', '键值存在')  # 修改默认键值对   如果key存在 则返回value值
print(ress,dicz)        # 111 {'k1': 111}

ress_ = dicz.setdefault('k1sss', '键值不存在')  # 键值不存在 则插入键值 并返回插入的value
print(ress_,dicz) # 键值不存在 {'k1': 111, 'k1sss': '键值不存在'}


dicz1 = {"k1": "nihao"}
dic1.update({'k1':"覆盖值",'k2': '插入新的值'})  # 字典更新
dic1.update(k4="另一种写法")
print(dic1)


