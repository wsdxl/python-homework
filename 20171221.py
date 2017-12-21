import csv
def feibonaqi(n):
    a=b=1
    for i in range(0,n):
        yield a 
        a,b=b,a+b    
    
with open('data.csv',mode='a',newline='') as f:
    w= csv.writer(f)
    for i in feibonaqi(10000):
        w.writerow([str(i)])
    f.close()
        
    
