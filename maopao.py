#冒泡排序
lists=[2,14,12,34,8,17,9]
n=len(lists)
for i in range(0,n):
    for j in range(i+1,n):
        if lists[i]>lists[j]:
            lists[i],lists[j]=lists[j],lists[i]
print(lists)