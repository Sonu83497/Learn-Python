'''
A function without a name is called as Anonymous function. it s also known as Lambda Function.
'''
lambda x: print(x)

lambda x,y: x+y
# anonymous function or lambda function
# single arguments
show = lambda x: print(x)
show(5)

# Two arguments
add = lambda x , y: (x+y)
print(add(10,20))

# return multiple
add_sub = lambda x,y : (x+y, x-y)
a, s = add_sub(5,2)
print(a)
print(s)

# 2 with default arguments
add = lambda x,y =3 :(x+y)
print(add(5))  
          
