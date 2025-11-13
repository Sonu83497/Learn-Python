''' logical_operators.py
This script demonstrates the use of logical operators in Python.

True and  False ==> False
True and  True  ==> True
False and False ==> False
False and True  ==> False
True or  False ==> True
True or  True  ==> True
False or False ==> False
False or True  ==> True 
not True  ==> False
not False ==> True
'''

x = 5
y = 10
print("x < 10 and y > 5:", x < 10 and y > 5)
print("x < 10 and y < 5:", x < 10 and y < 5)
print("x > 10 or y > 5:", x > 10 or y > 5)
print("x > 10 or y < 5:", x > 10 or y < 5)
print("not (x < 10):", not (x < 10))    
print("not (x > 10):", not (x > 10))
 