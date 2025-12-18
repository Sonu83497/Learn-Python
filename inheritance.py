#inheritance
class father:   #parent class
    money = 1000
    
    def show(self):
        print("Parent class instance method ")
        
    @classmethod
    def showmoney(cls):
        print("Parent class method :",cls.money)
        
    @staticmethod
    def stat():
        a = 10
        print("Parent class statics method :",a)

class Son(father):    #child class
    def disp(self):
        print("Child Class instance method")
s = Son()
s.disp()
s.show()
s.showmoney()
s.stat()