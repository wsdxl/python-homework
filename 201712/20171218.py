'''
python 数据写入csv文件
'''
import csv
with open('data.csv',mode='w') as f:
   m =csv.writer(f)
   m.writerow(['hello','python'])
f.close()