import os
import csv
num=int(input('Please enter a number:'))
def fol(num):
    n1,n2=0,1
    list=[n1,n2]
    for i in range(0,num):
        nth=n1+n2
        if nth<num:
            n1=n2
            n2=nth
            list.append(nth)  
    return list
        
def wriverfile(list):
    with open('data.csv',mode='w') as f:
        m =csv.writer(f)
        m.writerow(list)
    f.close()
   
list=fol(num) 
wriverfile(list)



