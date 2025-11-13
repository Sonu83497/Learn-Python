#to print numbers from 1 to 10 using while loop
'''
x = 1
while x <= 10:
    print(x)
    x = x + 1
''' 
#to print hello 10 times using while loop
'''
x = 1
while x <= 10:
    print("Hello")
    x = x + 1
'''
#to print sum of first n  numbers using while loop
'''
num = int(input("Enter a number: "))
sum = 0
i = 1
while i <= num:
    sum = sum + i
    i = i + 1
print("The sum of first", num, "numbers is:", sum)
'''
# write a program to prompt user to enter some name until entring name 

name = ""
while name !="Q":
    name = input("Enter the name (type 'Q' to stop): ")
print("Thanks for your confirmation:", name)