from abc import ABC, abstractmethod
class father(ABC):
    @abstractmethod
    def disp(self):  #abstract method
        pass
    def show(self):   #Concrete Method
        print("Concrete Method")

#my = father()  #not possible to create object of a anstract class
class child(father):
    def disp(self):
        print("Defining Abstract Method")
c = child()
c.disp()
c.show()
