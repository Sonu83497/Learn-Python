# this method overloading concept is not available in python
# so it will show error

class MyClass:
    def sum(self,a):
        print("1st sum method :",a)
    def sum(self):
        print("2st sum method :")
        
obj = MyClass()
obj.sum()
obj.sum(10)
        