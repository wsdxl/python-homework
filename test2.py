import os
import csv

#生成斐波那契数列
num=int(input('Please enter a number:')) 
n1,n2=0,1
list=[n1,n2]
while True:
    nth=n1+n2
    if nth>num:
        break
    n1=n2
    n2=nth
    list.append(nth)
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