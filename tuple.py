#with one element
b =10,
c = (10,)
d = (10)
print(type(b))
print(type(c))
print(type(d))

print('#with multiple elements')

x = (10,20,30,40)
y = (10,20,50,21.5,'Security')
z = 10,20,50,21.5,'Security'
print(type(x))
print(type(y))
print(type(z))

print('#Creating tuple with multiple tuple element')
d=(10,20,30,40)
e = (10,20,-50,21.5,'Security')
f = 10,20,-50,21.5,'Security'  # tuple e and f are same

print()

print('accessing tuple d :')
print("d[0] =", d[0])
print("d[1] =", d[1])
print("d[2] =", d[2])
print("d[3] =", d[3])
print()

print('accessing tuple e :')
print("e[0] =", e[0])
print("e[1] =", e[1])
print("e[2] =", e[2])
print("e[3] =", e[3])
print()

print('accessing tuple f :')
print("f[0] =", f[0])
print("f[1] =", f[1])
print("f[2] =", f[2])
print("f[3] =", f[3])


# index() method
a = (10,20,-50,21.5,'security')
#access tuple using for loop
a = (10,21.5,'security')
#with out index
print("Access without index")
for element in a:
    print(element)
print()

#with index 

print("Access With index ")
n = len(a)
print("Length of tuple : ",n)
for i in range(n):
     print(i, a[i])  
     
print()
print()
     
#Accessing using for loop
a = (10,20,-50,21.5,'security')
#without indexing
for x in a:
    print(x)

#with index 
n = len(a)
for i in range(n):
    print(i,a[i])

print()
print("#accessing using while loop")
a = (10,20,-50,21.5,'security')
n = len(a)
print(n)
#without indexing
i = 0
while i<n:
    print( a[i])
    i = i+1
#with indexing
i = 0
while i<n:
    print(i, a[i])
    i = i+1