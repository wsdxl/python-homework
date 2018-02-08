# class Foo:
#     def bar(am):
#         print('do sth')

# foo=Foo()
# foo.bar()

# class People:
#     hair='black'
#     def eat(a):
#         print('I can eat')
#     def buy(a):
#         print('I can shoping')
#     def love(a):
#         print('I fall in love')

# Tom=People()
# Tom.eat()
# Tom.buy()
# Tom.love()
# print(Tom.hair)

# class add:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b   
# x=add(3,4)
# print(x.a,x.b)

# class Test:
#     def prt(self):
#         print(self)
#         print(self.__class__)
 
# t = Test()
# t.prt()

# class People:  #定义一个People的类
#     name=''   #成员变量
#     age=0
#     __weight=0
#     def __init__(self,n,a,w): #定义构造方法
#         self.name=n
#         self.age=a
#         self._weight=w  #定义私有属性,私有属性在类外部无法直接进行访问
#     def speak(self):  # 定义方法
#         print('%s 说:我今年%d岁了 '%(self.name,self.age))
#         print('%s 说:我身高%dcm '%(self.name,self._weight))
# x=People('jack',30,170)
# print(x.name)
# print(x.age)
# print(x.__weight) # 报错，实例不能访问私有变量


# class Student(People): #Student 单继承 People类
#     grade=0
#     def __init__(self,n,a,w,g):  
#         People.__init__(self,n,a,w)  #调用父类构造方法
#         self.grade=g
    
#     def speak(self):
#         print('%s说：我%d岁了，我现在读%d年级了'%(self.name,self.age,self.grade))  #重写父类方法

# class Speaker: 
#     topic=''
#     name=''
#     def __init__(self,t,n):
#         self.topic=t
#         self.name=n
#     def speak(self):
#         print('我是%s,我是一个演说家,我演讲的主题是%s'%(self.name,self.topic))
    
# # class Sample()
# # x=Speaker('天空','jim')
# # x.speak()
# class Sample(Student,Speaker):
#     a=''
#     def __init__(self,n,a,w,g,t):
#         Student.__init__(self,n,a,w,g)
#         Speaker.__init__(self,t,n)

# test=Sample('make',18,170,5,'视频会议')
# test.speak()  #方法名同，默认调用的是在括号中排前地父类的方法


# class Parent:  #定义父类
#     def myMethod(self):
#         print('调用父类方法')

# class Child(Parent): #定义子类
#     def myMethod(self): #重写方法
#         print('调用子类方法')

# c=Child()
# c.myMethod()

# class Site:
#     def __init__(self, name, url):
#         self.name = name       # public
#         self.__url = url   # private
 
#     def who(self):
#         print('name  : ', self.name)
#         print('url : ', self.__url)
 
#     def __foo(self):          # 私有方法
#         print('这是私有方法')
 
#     def foo(self):            # 公共方法
#         print('这是公共方法')
#         self.__foo()
 
# x = Site('菜鸟教程', 'www.runoob.com')
# x.who()        # 正常输出
# x.foo()        # 正常输出

'''
类的专有方法：
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__div__: 除运算
__mod__: 求余运算
__pow__: 乘方
'''

class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
 
   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
 
v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)