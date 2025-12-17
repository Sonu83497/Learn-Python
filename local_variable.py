def show():
    x = 10  #local variable
    print(x) #accessing local variable inside function
show()
#accessing local variable outside function
# print(x)  #it will show error    


def add(y):
    x = 10
    print(x)
    print(x+y)
add(20)