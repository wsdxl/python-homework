'''
斐波那契数列，0,1,1,2,3,5,8,13...
'''
# num = int(input('请输入你要获得的数列的位数：'))
# n1 = 0
# n2 = 1
# count = 2
# if num <= 0:
#     print('你的输入不合法')
# elif num == 1:
#     print('输入的斐波那契数列为 %d' % num)
# else:
#     print('请输入斐波那契数列: ')
#     print(n1, ' , ', n2, end=' , ')
#     while num > count:
#         nth = n1 + n2
#         print(nth, end=' , ')
#         n1 = n2
#         n2 = nth
#         count += 1
'''
next解决阿莫斯特朗数
'''
import sys
num=int(input('请输入一个数：'))
if num<0:
    print('输入不合法')
n=len(str(num))
list=list(str(num))
it=iter(list)
sum=0
while True:
    try:
        sum=sum+int(next(it))**n
    except StopIteration as identifier:
        if num==sum:
            print('%d是阿莫斯特朗数'% num)
        else:
            print('%d不是阿莫斯特朗数'% num)
        sys.exit()
