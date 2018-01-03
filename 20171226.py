# class Foo:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def info(self):
#         print(self.name,self.age)

# x=Foo('jack',18)
# x.info()

class Animal:
    def eat(self):
	    print(self.name,'eat goods')
    def drink(self):
        print(self.name,'drink goods')
    def move(self):
        print(self.name,'move quick or slowly')
    
class Cat(Animal):
    def __init__(self,name):
        self.name=name
    def cry(self):
        print(self.name,'miaomiaomiao')

class Dog(Animal):
    def __init__(self,name):
        self.name=name
    def cry(self):
        print(self.name,'wang wang')



cat=Cat('小花猫 ')
cat.cry()
cat.eat()
cat.drink()
cat.move()
dog=Dog('大狼狗')
dog.cry()
dog.eat()
dog.drink()
dog.move()