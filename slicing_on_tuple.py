x = (101,102,103,104,105,106,107)
print("Original tuple :",x)
n = len(x)
print("Length of tuple : ",n)
for i in range(n):
    print(i, "=", x[i])
print()

print("From 1st position to 4th position")
a = x[1:5]
for i in a:
    print(i)
print()
print("From 0th position")
b = x[0:]
for i in b:
    print(i)
print()

print("From 5th position")
c = x[:5]
for i in c:
    print(i)
print()

print("Last 4 elements :")
d = x[-4:]
for i in d:
    print(i)
print()

print("From 0th position to 6th position stride 2")
e = x[0:7:2]
for i in e:
    print(i)
print()

print("Last 5 elements with [-5-(-3)]=2 elments towards right")
f = x[-5:-3]
for i in f:
    print(i)
print()




