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
print('phone:',phone)


'''
输入三个数，判断是一般三角形，直角三角形，等腰三角形还是等边三角形
'''
a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))
if a + b > c and a + c > b and b + c > a:
    if a == b != c or a == c != b or b == c != a:
        print('a,b,c组成等腰三角形')
    elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        print('a,b,c组成直角三角形')
    elif a == b == c:
        print('a,b,c组成等边三角形')
    else:
        print('a,b,c组成一般三角形')
else:
    print('a、b、c不构成三角形')
input('点击enter键退出')