'''
阿姆斯特朗数，如果一个n位正整数等于各位数字n次方的和，我们称该数为阿姆斯特朗数，
如：1*3+5*3+3*3=153，那么153就是阿姆斯特朗数。
1000以内的阿姆斯特朗数有：1,2,3,4,5,6,7,8,9，153,370，371,407
写一个程序检测输入的数是否是阿姆斯特朗数
'''

# 获取用户输入的数字
num = int(input("请输入一个数字: "))

# 初始化变量 sum
sum = 0
# 指数
n = len(str(num))

# 检测
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** n
   temp //= 10

# 输出结果
if num == sum:
   print(num,"是阿姆斯特朗数")
else:
   print(num,"不是阿姆斯特朗数")

# 获取指定期间内的阿姆斯特朗数
lower = int(input('最小值：'))
upper = int(input('最大值：'))
for num in range(lower, upper + 1):
    sum = 0
    n = len(str(num))
    temp = num
    while temp > 0:
        digit = temp % 10
        sum+=digit**n
        temp//=10
    if num==sum:
        print(num)



###############################################################################################

# sum=0
# m=100
# n=1
# while n<=m:
#     sum=sum+n
#     n+=1
# print('1到%d之间的和是：%d'%(m,sum))

# count=0
# while count<5:
#     print(count,'count小于5')
#     count+=1
# else:
#     print(count,'count等于5')

# list1=['baidu','jingdong','python','taobao']

# for value in list1:
#     if value=='python':
#         print('学习菜鸟教程')
#         break
#     print('测试数据：',value)
# else:
#     print('好尴尬啊')
# print('game over')

# for i in range(30,1,-2):
#     print(i)

# list1=['baidu','jingdong','python','taobao']
# for i in range(len(list1)):
#     print(i,list1[i])

# a=tuple(range(5))
# print(a)

# var = 10
# while var > 0:
#     var = var - 1
#     if var == 5:
#         continue
#     print(var)
# print('game over')

# pass语句
'''
pass是空语句，为了保持程序结构的完整性
一般用作占位语句
'''
for i in 'runoob':
    if i == 'o':
        pass
        print('执行pass语句')
    print(i)
print('good bye!')