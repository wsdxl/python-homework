# 元组使用小括号，列表使用方括号
# 元组的元素不能修改，列表的元素可以修改
# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当做运算符使用
# 元组和字符串类似，下标索引从0开始，可以进行截取和组合
# 元组中的元素时不可以删除的，但可以删除整个元组
# tup1=('hello','world','python','love')
# tup2=(1,2,3,4,5)
# tup3=6,7,8,9,0
# print(tup1)
# print(tup2)
# print(tup3)
# # 创建空元组
# tup4=()
# print(tup4)

# # 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当做运算符使用
# a=(40)  #不加逗号类型为整型
# print(type(a))
# b=(30,)
# print(type(b))

# # 访问元组
# tup1=('hello','world','python','love')
# tup2=(1,2,3,4,5,6,7,8)
# print(tup1[1])
# print(tup2[1:5])

# 元组不可以修改元组，但可以进行连接组合
x = (13, 35.98)
y = ('abc', 'lmn')
# x[0]=10
# print(x)

# 创建新元组
z = x + y
print(z)

# 删除元组
# 元组中的元素时不可以删除的，但可以删除整个元组
tup1 = ('hello', 'world', 'python', 'love')
tup = 1, 2, 3, 4, 5
tup2 = (6, 7, 8, 9)
# del tup1[1]  # 'tuple' object doesn't support item deletion
# del tup1
# print(tup1)

# 元组运算符
print(len(tup1), tup1.__len__())
print(tup + tup2)
print(tup2 * 2)
print(3 in tup)
print(8 not in tup)
for x in tup:
    print(x)

# 元组索引的截取
d = ('hello', 'world', 'python', 'love')
print(d[3])
print(d[-2])
print(d[1:])

# 元组的内置函数
tup1 = ('hello', 'world', 'python', 'love')
tup = ('i', 'love', 'you', 23, 56)
tup2 = (6, 7, 8, 9)
# print(max(tup))
print(max(tup1))
print(max(tup2))
# print(min(tup))
print(min(tup1))
print(min(tup2))

list = ['how', 'are', 'you']
print(list)
print(tuple(list))
print(tuple('hello'))
