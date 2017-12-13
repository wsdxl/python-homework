lists = ['hello', 'taobao', 'python', 'jingdong']
list1 = [2, 5, 4, 7, 9, 2]
list2 = ['xiaoming', 'M', 18, 13641878188]

# 列表末尾添加新的对象
lists.append(list1)
print(lists)

# 统计元素在列表中出现的次数；
print(list1.count(2))

# 在列表末尾一次性添加另一个序列中的多个值
lists.extend(list1)
print(lists)

# 找出某个值的第一个匹配项的索引位置
print(lists.index('phthon'))

# 将对象插入列表
lists.insert(1,list1)
print(lists)

# 移除列表中的元素，默认最后一个，
lists.pop(1)
print(lists)

# 移除列表中某个值的第一个匹配项
list2.remove(18)
print(list2)

# 反向排序
list1.reverse()
print(list1)

# 对原列表进行排序
list1.sort()
print(list1)

# 清空列表元素
list1.clear()
print(list1)

# 复制列表元素 ,没有看出效果
list1.copy()
print(list1)

print(lists)
lists.sort(key=len)
print(lists)
lists.sort(key=len,reverse=True)
print(lists)
lists.sort(reverse=True)
print(lists)