#!/usr/bin/python
#-*- coding: UTF-8 -*-

# try:
#     f=open('testlile','w',encoding="utf-8")
#     f.write('这是一个测试文件，用于测试异常!!')
# except IOError:
#     print('Error: 没有找到文件或读取文件失败')
# else:
#     print('内容写入文件成功')
#     f.close()

def temp_convert(var):
    try:
        return int(var)  
    except ValueError as Argument:
        print ("参数没有包含数字\n",Argument )
#调用函数 
temp_convert('abc')

    
# def functionName( level ): 
#     if level < 1: 
#         raise Exception("Invalid level!", level) 
# # 触发异常后，后面的代码就不会再执行

# class Networkerror(RuntimeError):
#     def __init__(self,arg):
#         self.arg=arg

# try:
#     raise Networkerror("Bad hostname")
# except Networkerror as e:
#     print (e.arg)

