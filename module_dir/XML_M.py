# -*- coding: UTF-8 -*- 
# XML 模块
import xml.etree.ElementTree as ET

tree = ET.parse('xo')

root = tree.getroot() # 根标签
print(root.tag)   # data


# 对文档树进行遍历
for child in root:
    print(child.tag,child.attrib) # con {'name': 'lili'}
    for i in child:
        print(i.tag,i.attrib)  # test {'name': 't1'}


# 只遍历 test节点
for node in root.iter('test'):
    print(node.tag,node.text)  #test 1


# 修改节点
# for node in root.iter('test'):
#    node.text = str(int(node.text)+1)
#    node.set('updated','yes')  # 设置标签属性
#
# tree.write('new_xml.xml')   # 将修改后的节点树写入新的xml文件


# 删除操作
# for c in root.findall('con'):
#     ran = int(c.find('range').text)
#     if ran >2:
#         root.remove(c)
#
# tree.write('new_xml_1.xml')

