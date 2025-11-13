num = bool(1)
print("The boolean value is:", num)
print("Type of the value is:", type(num))

num = bool(0)
print("The boolean value is:", num)
print("Type of the value is:", type(num))

num = bool(-5)
print("The boolean value is:", num)  # True
print("Type of the value is:", type(num))

num = bool("")
print("The boolean value is:", num)  # False
print("Type of the value is:", type(num))

num = bool("Hello")
print("The boolean value is:", num)  # True 
print("Type of the value is:", type(num))

num = bool([])
print("The boolean value is:", num)  # False    
print("Type of the value is:", type(num))

num = bool([1, 2, 3])
print("The boolean value is:", num)  # True 
print("Type of the value is:", type(num))

num = bool(None)
print("The boolean value is:", num)  # False        
print("Type of the value is:", type(num))

num = bool({1: "a", 2: "b"})    
print("The boolean value is:", num)  # True 
print("Type of the value is:", type(num))

num = bool({})  
print("The boolean value is:", num)  # False
print("Type of the value is:", type(num))

num = bool(10)
print("The boolean value is:", num)  # True 
print("Type of the value is:", type(num))

num = bool(10.5)
print("The boolean value is:", num)  # True 
print("Type of the value is:", type(num))

num = bool(-3.14)
print("The boolean value is:", num)  # True 
print("Type of the value is:", type(num))

num = bool(0.0) 
print("The boolean value is:", num)  # False
print("Type of the value is:", type(num))