'''
types of arguments :
1] actual arguments
2] formal arguments

# types of actual arguments 
1]Positional arguments
2]Keyword arguments
3]Default Arguments
4]Varible Length Arguments
5]Keyword Varible Length Arguments
'''

# Positional Arguments :
def pw(x,y):
    z = x**y
    print(z)
pw(5,2)

def pw(x,y):
    z = x**y
    print(z)
pw(2,5)

#Keyword arguments
def show(name,age):
    print(f"Name: {name} Age : {age}")
    show(name ="sonu", age = 21)

def show(age,name):
    print(f"Name: {name} Age : {age}")
    show(name ="sonu", age = 21)

#default arguments :
def show(name,age):
    print(f"Name: {name} Age : {age}")
    show(name ="sonu", age = 21)


def show(name,age=25):
    print(f"Name: {name} Age : {age}")
    show(name ="sonu")
    
#variable Length Arguments :
def add(x,y):
    z = x + y
    print("Addition :",z) 
add(5,2)

def add(*num):
    z = num[0] + num[1] + num[2] + num[3]
    print("Addition :",z)
add(5,2,3,5)

#keywoard variable length arguments
def add(**num):
    z = num['a']*num['b']*num['c']
    print("Addition :",z)
add(a=10,b=20,c=30)
