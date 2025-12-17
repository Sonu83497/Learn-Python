'''
if local variable and global variable has same name then the function by default refers to the local variable and ignorws the global variable.
'''
a = 50
def show():
    a = 10
    print("Local :",a)
show()
print("Global :",a)