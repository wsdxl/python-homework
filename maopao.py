# #冒泡排序
# lists=[2,14,12,34,8,17,9]
# n=len(lists)
# for i in range(0,n):
#     for j in range(i+1,n):
#         if lists[i]>lists[j]:
#             lists[i],lists[j]=lists[j],lists[i]
# print(lists)



# def bubble_sort(list1):
#     # 冒泡排序
#     n = len(list1)
#     for i in range(0, n):
#         for j in range(i + 1, n):
#             if list1[i] > list1[j]:
#                 list1[i], list1[j] = list1[j], list1[i]
#     return list1

# list1 = [1,20,13,16,5,18]
# s=bubble_sort(list1)
# print(s)

lists=[2,14,12,34,8,17,9]
n=len(lists)
for i in range(0,n):
    for j in range(i+1,n):
        if lists[i]>lists[j]:
            lists[i],lists[j]=lists[j],lists[i]
print(lists)