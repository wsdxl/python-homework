# var1=100
# if var1:
#     print('1表达式条件为true')
#     print(var1)
# var2=0
# if var2:
#     print('2表达式条件为true')
#     print(var2)
# else:
#     print('Good bye')

# age=int(input('请输入你家狗狗的年龄：'))
# print("")
# if age<0:
#     print('你是在逗我吧！')
# elif age==1:
#     print('相当于14岁的人')
# elif age==2:
#     print('相当于22岁的人')
# elif age>2:
#     human=22+(age-2)*5
#     print('对应人类的年龄',human)
# input('点击enter键退出')

# number=7
# guess=0
# print('数字猜谜游戏')
# while number !=guess:
#    guess= int(input('请输入您猜的数字：'))
#    if guess<number:
#         print('猜的数字小了...')
#    elif guess>number:
#         print('猜的数字大了...')
#    elif guess==number:
#         print('恭喜你猜对了...')

num=int(input('请输入一个数：'))
if num%2==0:
    if num%3==0:
        print('您输入的数字可以整除2和3')
    else:
        print('您输入的数字可以整除2但不能整除3')
else:
    if num%3==0:
        print('您输入的数字可以整除3但不能整除2')
    else:
        print('您输入的数字既不能整除2也不能整除3')