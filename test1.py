# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if x>=0:
#         return x
#     else:
#         return -x

# print(my_abs('a'))
'''
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程
ax2 + bx + c = 0 的两个解
'''
import math  
def quadratic_equation(a, b, c):  
    if a==0:
        x1=x2=-c/b
        return x1,x2
    elif a!=0 and b**2-4*a*c>0:
        x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
        return x1,x2
    elif a!=0 and b**2-4*a*c==0:
        x1=x2= (-b)/2*a
        return x1,x2
    else:
        return '无解'
        


print (quadratic_equation(1, 2, 3))
print (quadratic_equation(1, -6, 5))
print (quadratic_equation(0, 2, 3))

