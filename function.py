def add():
    x = 10
    y = 20
    s = x + y
    print(s)

#calling function
add()
add(20)
add(10.56)
add("python")


#defining function one time
def disp():
    name = "cybersecurity"
    print("Welcome Hacking World !")
#calling function as many time as we need 
disp()

#seprate function for addition 
def add(y):
    x = 10
    c = x + y
    print(c)
add()

#seprate function for subtraction
def sub():
    x = 10
    y = 20
    c = x - y
    print(c)
sub()


#actual and formal arguments 
def add (x,y):  # <=== Formal Arguments
    c = x + y
    print(c)
add(10,20)     # <=== actual Arguments


