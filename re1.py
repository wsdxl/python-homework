'''
正则表达式
group([group1, …]): 
获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回。group1可以使用编号也可以使用别名；编号0代表整个匹配的子串；不填写参数时，返回group(0)；没有截获字符串的组返回None；截获了多次的组返回最后一次截获的子串。
groups([default]): 
以元组形式返回全部分组截获的字符串。相当于调用group(1,2,…last)。default表示没有截获字符串的组以这个值替代，默认为None。
groupdict([default]): 
返回以有别名的组的别名为键、以该组截获的子串为值的字典，没有别名的组不包含在内。default含义同上。
start([group]): 
返回指定的组截获的子串在string中的起始索引（子串第一个字符的索引）。group默认值为0。
end([group]): 
返回指定的组截获的子串在string中的结束索引（子串最后一个字符的索引+1）。group默认值为0。
span([group]): 
返回(start(group), end(group))。
expand(template): 
将匹配到的分组代入template中然后返回。template中可以使用\id或\g<id>、 \g<name>引用分组，但不能使用编号0。\id与\g<id>是等价的；但\10将被认为是第10个分组，如果你想表达 \1之后是字符'0'，只能使用\g<1>0
'''
# !/usr/bin/python
# -*- coding: UTF-8 -*-
# import re
# key = r"<html><body><h1>hello world<h1></body></html>"  #这段是你要匹配的文本
# p1 = r"(?<=<h1>).+?(?=<h1>)"  #这是我们写的正则表达式规则，你现在可以不理解啥意思
# pattern1 = re.compile(p1)  #我们在编译这段正则表达式
# matcher1 = re.search(pattern1, key)  #在源文本中搜索符合正则表达式的部分
# print (matcher1.group(0))  #打印出来

# import re 
# key = r"javapythonhtmlvhdl"#这是源文本 
# p1 = r"python"#这是我们写的正则表达式 
# pattern = re.compile(p1)
# matcher1 = re.search(pattern,key)
# print (matcher1.group(0))

# import re
# print(re.match('www', 'www.runoob.com').span())
# print(re.match('com', 'www.runoob.com'))

# import re
# line = "Cats are smarter than dogs"
# matchObj = re.match( r'(.*) are (.*?) (.*)', line, re.M|re.I)
# if matchObj:
#    print ("matchObj.group() : ", matchObj.group())
#    print ("matchObj.group(1) : ", matchObj.group(1))
#    print ("matchObj.group(2) : ", matchObj.group(2))
#    print ("matchObj.group(3) : ", matchObj.group(3))
# else:
#    print ("No match!!")

# print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.search('com', 'www.runoob.com').span())   # 不在起始位置匹配

# import re
# line = "Cats are smarter than dogs";
# searchObj = re.search( r'(.*) are (.*?) (.*)', line, re.M|re.I)
# if searchObj:
#    print ("searchObj.group() : ", searchObj.group())
#    print ("searchObj.group(1) : ", searchObj.group(1))
#    print ("searchObj.group(2) : ", searchObj.group(2))
#    print ("searchObj.group(3) : ", searchObj.group(3))
# else:
#    print ("Nothing found!!")
'''
re.match与re.search的区别
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
而re.search匹配整个字符串，直到找到一个匹配。
'''
# import re
# line = "Cats are smarter than dogs"
# matchObj = re.match( r'dogs', line, re.M|re.I)
# if matchObj:
#    print ("match --> matchObj.group() : ", matchObj.group())
# else:
#    print ("No match!!")
# matchObj = re.search( r'dogs', line, re.M|re.I)
# if matchObj:
#    print ("search --> matchObj.group() : ", matchObj.group())
# else:
#    print ("No match!!")

'''
检索和替换
Python 的re模块提供了re.sub用于替换字符串中的匹配项。
repl 参数是一个函数
'''
# import re
# phone = "2004-959-559 # 这是一个电话号码"
# # 删除注释
# num=re.sub('#.*$',"",phone)
# print(num)
# # 移除非数字的内容
# num=re.sub("\D","",phone)
# print(num)

# import re

# # 将匹配的数字乘于 2
# def double(matched):
#     value = int(matched.group('value'))
#     return str(value * 2)

# s = 'A23G4HFD567'
# print(re.sub('(?P<value>\d+)', double, s))

import re
s = '2017-11-27'
print(re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1', s))