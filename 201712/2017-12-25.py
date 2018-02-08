class Fib:
    def __init__(self,counter):
        self.couter = counter
        self.a ,self.b = 0,1

    def __iter__(self):
        return  self

    def __next__(self):
        self.a ,self.b = self.b,self.a+self.b

        if self.a > self.couter:
            raise  StopIteration()
        return self.a

for i in Fib(10000):
    print(i)