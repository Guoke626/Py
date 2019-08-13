
#  元组 （） 不能修改，添加     只能查询 下标从0开始
tup=('xiaoming','tom','jack')
print(tup[0])
print(tup[1])
print(tup[2])
print('元组的长度：',len(tup))

#  列表 [] 进行增删改查

list=[123,234,345,456,567,678,789]
print('列表的长度：',len(list))
print(list[1:4])
print(list[:4])
print(list[0:7:2])
print(list[::-1])

# 添加数据,在尾部追加
list.append(998)
print(list)

# 指定位置添加元素
list.insert(1,700)
print(list)
'''
list+=[999]
print(list)
'''

# 更新
list[2]=123
print(list)

#删除
list.remove(123)
print(list)
del list[0]
print(list)
list.pop(0)
print(list)

# 字典{键：键值，键：键值}
dict={'name':'小明','age':18,'sex':'男'}

#  通过key获取value
uname=dict['name']
print(uname)
uage=dict['age']
print(uage)
usex=dict['sex']
print(usex)
#  添加
dict['tel']='18810159185'
print(dict)
#  更新
dict['age']=21
print(dict)