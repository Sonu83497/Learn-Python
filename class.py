class Student: #create class
    college_name = "Vikrant University Gwalior"  
    name = "anonymous"  
    #Default constructor
    def __init__(self):
        pass 
    # parameterized constructors
    def __init__(self,name,marks):
        self.name = name  #obj attr > class attr
        self.marks = marks
        print("Adding new student in database..")  
    def welCome(self):
        print("Welcome Coding world !",self.name)    
        
    def get_marks(self):
        return self.marks  

s1 = Student("Karan",98)  #object
print(s1.name,":",s1.marks)
print(s1.college_name)
s1.welCome()
print(s1.get_marks())

class mobile :
    def __init__(self):
        self.model = "RealMe X"
    def show_model(self):
        print("Model :",self.model)
  
class masterClass(object):
    def show(self):
        print("I am a sonu prajapati !")
x = masterClass()
x.show()


class myClass:
    def show(self):
        print("I am a Hacker !")
x = myClass()
print(x)
x.show()









