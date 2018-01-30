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


class People:
    name=''
    age=0
    __weight=0
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.__weight=w
    def speak(self):
        print('%s说:我今年%d岁了!'%(self.name,self.age))

people=People('xiaoming',18,100)
people.speak()