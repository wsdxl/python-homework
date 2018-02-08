# class MyTest:
#     a=1234
#     def f(self):
#         print(self.a)

# test=MyTest() ##创建对象（实例化）
# test.f() ##通过对象调用类的方法
# print(MyTest.a)  #通过类名访问其属性；

# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get('http://118.31.19.120:3000/signin')

# class LoginPage:
#     username_id='name'
#     password_id='pass'
#     loginbtn_classname='span-primary'
#     def userLogin(self,username,password):
#         driver.find_element_by_id(self.username_id).send_keys(username)
#         driver.find_element_by_id(self.password_id).send_keys(password)
#         driver.find_element_by_class_name(self.loginbtn_classname).click()
# login=LoginPage()
# login.userLogin('helloworld',123456)


# class People:
#     name=''
#     age=0
#     __weight=0
#     def __init__(self,n,a,w):
#         self.name=n
#         self.age=a
#         self.__weight=w
#     def speak(self):
#         print(' %s 说:我今年 %d 岁了,我体重 %d 斤!'%(self.name,self.age,self.__weight))

# # people=People('xiaoming',18,100)
# # people.speak()

# class Student(People):
#     grade=0
#     def __init__(self,n,a,w,g):
#         People.__init__(self,n,a,w)
#         self.grade=g
#     def speak(self):
#         print(' %s 说:我今年 %d 岁了,我在读 %d 年级！'%(self.name,self.age,self.grade))
# # student=Student('xiaohong',9,60,2)
# # student.speak()

# class Speaker():
#     name=''
#     topic=''
#     def __init__(self,n,t):
#         self.name=n
#         self.topic=t
#     def speak(self):
#         print(' %s 说：我是一个演说家,我演讲的主题是 %s'%(self.name,self.topic))
# # speaker=Speaker('jack','python')
# # speaker.speak()

# #多重继承

# class Sample(Speaker,Student):
#     a=''
#     def __init__(self,n,a,w,g,t):
#         Speaker.__init__(self,n,t)
#         Student.__init__(self,n,a,w,g)
    
# test=Sample('Tim',16,50,6,'Java')
# test.speak()

# #方法重写
# class Parent:
#     def myMethod(self):
#         print('调用父类方法')   

# class child(Parent):
#     def myMethod(self):
#         print('调用子类方法')

# c=child()
# c.myMethod()

# #类的私有属性实例如下：
# class Counter:
#     publicCount=0  #公共变量
#     __privateCount=0 #私有变量
#     def count(self):
#         self.publicCount+=1
#         self.__privateCount+=1
#         print(self.__privateCount)

# counter=Counter()
# counter.count()
# counter.count()
# print(Counter.publicCount)
# print(counter.publicCount)
# # print(counter.__privateCount)

#运算符重载




