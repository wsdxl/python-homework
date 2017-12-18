import os
import csv

#生成斐波那契数列
# num=int(input('Please enter a number:'))
n1,n2,nth=0,1,0
list=[n1,n2]
while True:
    nth=n1+n2
    n1=n2
    n2=nth
    list.append(nth)
    for i, j in enumerate(list):
        print (i)
    if i>1000000:
        break
print(list)

#将斐波那契数列写入data.csv文件
with open('data.csv',mode='w') as f:
   m =csv.writer(f)
   m.writerow(list)
f.close()

#读取data文件中的数据
filepath=os.path.join(os.getcwd(),'data.csv')
f=open(filepath)
reader=csv.reader(f)
list1=[]
for i in reader:
    list1.extend(i)
print(list1)

# lower = int(input('最小值：'))
# upper = int(input('最大值：'))
# for num in range(lower, upper + 1):
#     sum = 0
#     n = len(str(num))
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit**n
#         temp //= 10
#     if num == sum:
#         print(num)


