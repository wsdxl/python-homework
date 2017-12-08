import os
import csv

filepath = os.path.join(os.getcwd(), 'data',
                        'userinfo.csv')  # get csv file path
f = open(filepath)  # open file
reader = csv.reader(f)  # read file
users = []  # define one list
next(reader, None)  # ignore first line
for i in reader:  # Traverse every line's value
    users.append(i) # 将值追加到列表中
print(users)