'''
作业：
1、判断从键盘输入的成绩，大于90优秀，60-90,及格，0-60不及格，其他“不合法分数输入”
2、“qwertyuiopasdfghjklzxcvbnm”
a,截取前三个;
b,截取第二个到倒数第二个
c，一个间隔一个截取
3，a=10,b=20 交换a,b的值，两种方法
'''
# 第一题
score=float(input('score:'))
if score<60 and score>=0:
    print('不及格')
elif score>=60 and score<=90:
    print('及格')
elif score>90 and score<=100:
    print('优秀')
else:
    print('不合法分数输入')

#第二题
a="qwertyuiopasdfghjklzxcvbnm"
print(a[:3])
print(a[1:-1])
print(a[::2]) # 如果a[0]也算
print(a[1::2]) #如果a[0]不算
# 第三题
a=10;b=20
#方法1
a,b=b,a
print('a=',a,'b=',b)
#方法2
a=a+b
b=a-b
a=a-b
print('a=',a,'b=',b)