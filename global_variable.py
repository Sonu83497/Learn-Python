a = 50  #global variable
def show():
    x = 10   #local variable
    print(x) #access local variable inside function
    print(a) ##access global variable inside function
show()
#access global variable outside function
print("Global Variable :",a)