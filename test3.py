def fab(max): 
   n, a, b = 2, 0, 1 
   nth=0
   list = [a,b] 
   while n < max: 
       nth=a+b 
       a, b = b,nth
       list.append(nth)
       n = n + 1 
   return list
print(fab(4))