# import sys

# def feina(n):
#     a,b,counter=0,1,0
#     if counter>n:
#         return
#     yield a
#     a,b=b,a+b
#     counter+=1

# f=feina(10)

# while True:
#     try:
#         print(next(f),end='')
#     except StopIteration:
#         sys.exit()

# def generator1():
#     for i in range(10):
#         yield i

# for item in generator1():
#     print(item)

# my_str='dfg'
# my_iter=iter(my_str)
# print(next(my_iter))

def feibonaqi(n):
    a=b=1
    for i in range(0,n):
        yield a
        a,b=b,a+b
a=feibonaqi(100)
import os
import csv
with open('data.csv',mode='w') as f:
   m =csv.writer(f)
   m.writerow(a)
f.close()

filepath=os.path.join(os.getcwd(),'data.csv')
f=open(filepath)
reader=csv.reader(f)
list1=[]
for i in reader:
    list1.extend(i)
print(list1)
