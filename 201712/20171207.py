"""
字典
键必须是唯一的，但值不必；
值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组
"""
# dict = {'Alice': '2345', 'Tom': '2323', 'jack': '2324'}
# dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# # print(dict['Alice'])
# # print(dict1['Age'])
# # print(dict1['Alice']) #字典里没有的键会报错，KeyError: 'Alice'

# # 修改字典
# dict1['Age']=9  #修改信息
# dict['Fate']='2325'  #添加信息
# print(dict1['Age'])
# print(dict)

#删除字典元素
dict = {'Alice': '2345', 'Tom': '2323', 'jack': '2324'}
del dict['Alice']  #删除元素
print(dict['Alice'])
del dict     #删除字典
dict.clear()  #清空字典元素
print(dict)

"""
 字典键的特性
 字典值可以是任何的python对象，既可以是标准的对象，也可以是用户定义的，但键不行，两个重要的点需要记住：
 1）不允许同一个键出现两次,创建时如果同一个键被赋值两次，后－个值会被记住
 2）能必须不可变，所以可以用数字，字符串或元组充当， 而用列表就不行
"""
