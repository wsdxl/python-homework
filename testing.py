# a=input('\n\n\n\n\n enter over!')
# print(a,end='')

# import sys; x='john';sys.stdout.write(x*3);print('good')
# import sys
# print('================Python import mode==========================');
# print ('命令行参数为:')
# for i in sys.argv:
#     print (i)
#     print ('\n python 路径为',sys.path)
# from sys import argv,path
# print('================python from import===================================')
# print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

# help(max)
# a=111
# print(type(111))
# print(isinstance(a,int))
# a='rtuytrtyuiiuygf'
# print(a.isalnum())
# print(a.isdigit())
# print(a.islower())
# print(a.isupper())
# print(a.upper())
# print(a.lower())
# print(a.lstrip())
# print(a.split('day',))
# list = ['Google', 'Java', 1997, 2000]
# # del list[2]
# list.clear()
# print(list)
a = ['a', 'm', 'u','d','e'] 
n = [1, 2, 3] 
# b=[a,n]
# print(b[0],b[0][1])
# print(list(a))
# a.append(n)
# a.extend(n)

# print(a.index('b'))
# a.insert(1,n)
# print(a)

# a.pop(2)
# print(a)
# a.reverse()
# print(a)
# a.sort()
# a.copy()
# print(a)

# student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose','Jim'}
# print(student) 

# a = set('abracadabra')
# b = set('alacazam')
# print(a)
# print(b)
# print(a-b)
# print(a|b)
# print(a&b)
# print(a^b)

dict = {'Name': 'John', 'Age': 7, 'Class': 'First'}

# print(dict['Name'],dict['Age'])
# dict['Age']=9
# dict['Scool']='midlle'
# print(dict)
# print(dict)
# print(str(dict))


# print(dict.get('Name'))
# print(dict['Name'])
# print('Name' in dict)
# dicts=dict.items()
# list1=list(dicts)
# for i in list1:
#     print(i)

dict = {'Name': 'John', 'Age': 7, 'Class': 'First'}
# a=dict.keys()
# b=dict.values()
# print(a)
# print(b)
# dict.pop('Name')
# print(dict)
dict.popitem()
print(dict)