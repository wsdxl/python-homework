'''
九九乘法表
'''
s = 1
for i in range(1, 10):
    for j in range(1,i+1):
        s =str( j * i)
        print('{}*{}={}\t'.format(j,i,s),end='')
    print()

'''
九九加法表
'''
s = 1
for i in range(1, 10):
    for j in range(1,i+1):
        s =str( j + i)
        print('{}+{}={}\t'.format(j,i,s),end='')
    print()
'''
求10-100中能被3或5整除的数的和
'''
s = 0
for i in range(10, 101):
    if i % 3 == 0 or i % 5 == 0:
        s+=i
print(s)

'''
求从1-100的奇数和
'''
sum=0
for i in range(1,100,2):
    sum+=i
print(sum)
'''
3.随机生成一个手机号码（13xxxxxxxxx,15xxxxxxxxx,17xxxxxxxxx,18xxxxxxxxx）
'''
import random
first_num = '1'
phone_secound = str(random.choice([3, 5, 7, 8]))
phone = first_num + phone_secound
for i in range(9):
    phone = phone + str(random.randint(0, 9))
print(phone)