#To print characters present in the given string using for loop
'''string = input("Enter a string: ")
for char in string:
    print(char)

'''
#To print characters present in the given string index wise using for loop
'''
s = input("Enter a string: ")
i = 10
for x in s:
    print("Character at index", i, "is", x)
    i = i + 1
'''
#To print numbers from 1 to n using for loop    
'''
n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(i) 
'''

#to print hello 10 times
'''
n = int(input("Enter a number: "))
for i in range(n):
    print("Hello")
'''

#To display odd numbers
'''
num = int(input("Enter a number: "))

for x in range(0, num + 1):
    if x % 2 != 0:
        print(x)
'''

#To display even numbers
'''
num = int(input("Enter a number: "))
for x in range(2, num + 1):
    if x % 2 == 0:
        print(x)
'''

#To display numbers in reverse order
'''
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    print(i)
'''

#to print sum of numbers present inside a list
'''
list = eval(input("Enter a list of numbers: "))
sum = 0
for num in list:
    sum = sum + num
print("The sum of the numbers in the list is:", sum)
'''

#To print multiplication table of a given number
'''
n = int(input("Enter a number to display its multiplication table: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
'''

#To print factorial of a given number
'''
n = int(input("Enter a number to find its factorial: "))    
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print("The factorial of", n, "is:", factorial) 
'''
#To print Fibonacci series up to n terms

n = int(input("Enter a number: "))
a, b = 0, 1
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
    
