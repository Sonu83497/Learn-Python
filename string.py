'''
s = "Sonu Prajapati"
print(s[0:4])  # Output: Sonu
print(s[5:])   # Output: Prajapati
print('P' in s)
print('z' in s)
'''

'''
#By using Index 
s = input("Enter some string :")
i = 0
for x in s:
    print("The character present at positive index {} and at negatives index {} is {}".format(i,i-len(s),x))
    i = i+1
'''

'''
#accesssing characters by using slice operators 
s = ("Learning Python is very very easy !!!!")
s [1:5:1]
print(s)
'''

'''
#mathematical operator for string :
print("Cyber"+"Security")
print("sonu "*5)
'''

'''
#Checking membership in string
s = input("Enter Main String : ")
subs = input("Enter Sub String :")
if subs in s:
    print(subs,",is found in main string !")
else:
    print(subs,",is not found a main string")
'''

'''
#comparison of String :
s1 = input("Enter First String :")
s2 = input("Enter second String :")
if s1 == s2:
    print("Both String Are Equal !")
elif s1<s2:
    print("First string is Less than second string !")
else:
    print("First string is grater than second string !")
'''

'''
#removing space from the string 
city = input("Enter your city name :")
scity  =city.strip()
if scity == 'Morena':
    print("Hello Morena -- Welcome")
elif scity == 'Gwalior':
    print("Hello Gwalior -- Hello")
elif scity == 'indore':
    print("Hello Indore -- namste")
else:
    print("You are entered city invalid ")
'''

'''
#finding substring [find()]
s = "Learning Python is very very easy "
print(s.find("Python"))
print(s.find("java"))
print(s.find("v"))
print(s.find("very"))


s = "sunilkumarpython"
print(len(s))
print(s.find('a'))
print(s.find('a',7,15))
print(s.find('z',7,15))
'''

'''
#finding through string [index()] let me check: fir se karna yah run nahi hua tha code
from operator import index

s = input("Enter main string :")
subs = input("Enter sub String :")
try:
    n =index(subs)
except ValueError:
    print("Substring Not Found")
else:
    print("Substring Found")
'''

'''
#counting substring in the given string
s = "abcabcabacabcdda"
print(s.count("a"))
print(s.count('abc'))
'''

'''
#replacing a string with another string
s = 'abcabcabcabcabc'
print(s.replace("a","c") )
'''

'''
#Splitting of String 
s = "Cyber Security Expert "
l = s.split(' ')
for x in l: 
    print(x) 
    
    
s = "02-08-2004"
l = s.split('-')
for x in l:
    print(x)
'''

'''
#joing of String
t = ("sonu" , "Monu" , "Tarun" , "Arun")
s = "^^".join(t)
print(s)
'''

'''
#changing case of a string 
s = "Sonu go To COLLege IN GwalioR"
#upper case
print(s.upper())
#lower case
print(s.lower())
#swapcase
print(s.swapcase())
#title cse
print(s.title())
#capitalize case 
print(s.capitalize())
'''


'''
#checking starting and ending part of the string 

s = 'sonu Prajapati'
print(s.startswith('s'))
print(s.endswith('y'))
'''


#formatting the string 
name = "sonu"
salary = 100000
age = 21

print("{}'s salary is {} and his age is {}".format(name,salary,age)) 
print("{0}'s salary is {1} and his age is {2}".format(name,salary,age))
print("{x}'s salary is {y} and his age is {z}".format(z=age,y=salary,x=name))

