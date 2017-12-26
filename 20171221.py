def fobo(n):
    n1, n2 = 0, 1
    for i in range(0, n):
        yield n1
        n1, n2 = n2, n1 + n2


import csv
with open('data.csv', mode='a', newline='') as f:
    w = csv.writer(f)
    for i in fobo(100):
        w.writerow([str(i)])
    f.close()
