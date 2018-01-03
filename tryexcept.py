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

# def temp_convert(var):
#     try:
#         return int(var)
#     except ValueError as Argument:
#         print ("参数没有包含数字\n",Argument )
# #调用函数
# temp_convert('abc')

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

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again   ")

# import sys

# try:
#     f = open('testline')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise

# import sys
# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except IOError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()

# def this_fails():
#      x = 1/0
# try:
#     this_fails()   
# except ZeroDivisionError as err:
#     print('Handling run-time error:', err)


# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise

# class MyError(Exception):
#     def __init__(self, value):
#         self.value = value
#     def __str__(self):
#         return repr(self.value)

# try:
#     raise MyError(2*2)
# except MyError as e:
#     print('My exception occurred, value:', e.value)

# raise MyError('oops!')

# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world!')

# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("division by zero!")
#     else:
#         print("result is", result)
#     finally:
#         print("executing finally clause")
        
# # divide(4,2)
# # divide(4,0)
# divide('4','1')

with open("data.csv") as f:
    for line in f:
        print(line, end="")
