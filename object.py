'''
object_name = class_name()
object_name = class_name(arguments)
'''

# class Mobile:
#     def __init__(self):
#         self.model = "samsung m14"
    
#     def show_model(self):
#         print("Model : ",self.model)
# #Creating Object of  class
# samsung = Mobile()
# #print("samsung")
# #accessing variable from outside class 
# print(samsung.model)
# #assign variable a new value
# samsung.model = "samsung pro"
# print(samsung.model)
# #accessing method from outside class 
# samsung.show_model()



# class Mobile :
#     def __init__(self):
#         self.model = 'Samsung M14 5G'

#     def show_model(self):
#         price = 10000   #local variable
#         print("Model :",self.model, "and Price :",price)
# samsung = Mobile()
# #accessing method from outside class 
# samsung.show_model()

class mobile:
    #contructor
    def __init__(self,m):
        self.model = m
    
    def show_model(self,p):
        price = p    #local variable
        print("Model :",self.model, "and Price",price)
#passing arguments to constructor
samsung = mobile("Samsung M14 5G")
#accessing method from outside class
samsung.show_model(2000)
        










