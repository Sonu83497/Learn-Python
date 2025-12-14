#Accessing using while loop
'''
a = [10,20,11.3,15.5,"CyberSecurity"]
print("Accessing List using while loop")
n = len(a)
print(n)
i=0
while i<n:
    print(i,"=",a[i])
    i +=1 
''' 
# Deletion 
'''
a = [10,20,11.3,15.5,"CyberSecurity"]
del a[2]
# Deleting Element
print(a)
# Deleting Entire List
del a


a = [10,20,11.3,15.5,"CyberSecurity"]
print("Before Deletion :")
print(a)
print()
#Deleting single element of list
del a[0]
print(a)
#Deleting entire list
del a
print(a)  # it will show error as list a has been deleted
'''

# append () function
'''
a = [10,20,11.3,15.5,"CyberSecurity"]

print("Before Appending :")
for element in a:
    print(element)
    
# Appending an element

a.append(100)
print()
print("After Appending")
for element in a:
    print(element)
'''

#Getting User Input
'''
a = []
n = int(input("Enter Number of element :"))
for i in range(n):
    a.append(int(input("Enter Element :")))
    
print("List :")
for element in a:
    print(element)
'''

#insert () function
'''
a = [10,20,11.3,15.5,"CyberSecurity"]
print("Before :",a)
a.insert(2,'Subscribe')
print("After :",a)

for element in a:
    print(element)
'''

#with list() function
'''
#creating empty list using list function
a = list()
print(a)
print(type(a))

#creating list using list function and range function
b = list(range(0, 5))
print(b)
print(type(b))
'''

#pop () funstion
''' 
a = [10,20,11.3,15.5,"CyberSecurity"]
print("Before POP :",a)
a.pop()
print("After POP :",a)
for element in a:
    print(element)
'''
#pop (n) function
'''
a = [10,20,11.3,15.5,"CyberSecurity"]
print("Before POP :",a)
n = a.pop(2)
print("After POP :",a)
for element in a:
    print(element)
print("Removed element",n)
'''

#remove (element) method
'''
a = [70,10,30,20,90,'Security']
print("Before remove : ",a)
a.remove(10)
print("After remove : ",a)
for element in a :
    print(element)
'''

#index () method
'''
a = [70,10,30,20,90,'Security']
num = a.index(10)
print(num)
'''

#reserve () function
'''
a = [70,10,30,20,90,'Security']
print("Before Reserve :",a)
a.reverse()
print("After Reserve : ",a)
'''

#extend () method
'''
a = [70,10,30,20,90,'Security']
b = [100,200,300]
print("Before Extent : ",a)
a.extend(b)
print("After Extend :",a)
'''
#count () function
'''
a = [70,10,30,30,90,'Security']
num = a.count(30)
print(num)
'''

#sort () function
'''
a = [10,5,90,10,30]
print("Before Sort",a)
a.sort()
print("After Sorting : ",a)

for element in a:
    print(element) 
'''

#clear() function
'''
a = [10,5,90,10,30]
print("Before Clear :",a)
a.clear()
print("After Clear",a)
'''
