'''
迭代器
'''
# list=[1,2,3,4]
# s=iter(list)
# for i in s: 
#     print(i,end=' ')

list1=[5,2,3,4]
import sys
m=iter(list1)
while True:
    try:
        print(next(m),end=' ')
    except StopIteration:
        sys.exit()