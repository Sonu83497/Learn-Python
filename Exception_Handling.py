#without Exception Handling
a = 10
b = 0
d = a/b
print(d)
print("Rest of the code")

#with exception handling
a = 10
b = 0
try:
    d = a/b
    print(d)
    print("Inside Try")
except ZeroDivisionError:
    print("Division by Zero Not Allowed")
print("Rest of Code")

# Else Statement

a = 10
b = 5
try:
    d = a/b
    print(d)
    print("Inside Try")
except ZeroDivisionError:
    print("Division by zero ot allowed")
else:
    print("Inside Else")
print("Rest of the code")

a = 10
b = 0
try:
    d = a/b
    print(d)
    print("Inside Try")
except ZeroDivisionError as o:
    print(o)
print("Rest of the code")
NameError

a = 10
b = 0
try:
    d = a/b
    print(d)
except ZeroDivisionError as obj:
    print(obj)
except NameError as ob:
    print(ob)
print("Rest of the code")

a = 10
b = 0
try:
    d = a/b
    print(d)
except (NameError,ZeroDivisionError) as obj:
    print(obj)
print("Rest Of the Code")