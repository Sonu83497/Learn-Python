class Add:
    def result(self,a,b):
        print("Addition :",a + b)

class Mul(Add):
    def result(self, a, b):
        print("Multi :",a * b)

m = Mul()
m.result(10,20)


#method overrriding
class Add:
    def result(self,a,b):
        print("Addition :",a + b)

class Mul(Add):
    def result(self, a, b):
        print("Multi :",a * b)

m = Mul()
m.result(10,20)

s = Add()
s.result(10,20) 

#method call super()

class Add:
    def result(self,x,y):
        print("Addition :",x + y)
class multi(Add):
    def result(self, a, b):
        super().result(10, 20)
        print("Multiplication :", a * b)

m = multi()
m.result(10,20)