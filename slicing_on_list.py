x = [101, 102, 103, 104, 105, 106, 107]
print("Original List :" ,x)
n = len(x)
for i in range (n):
    print(i, "=", x[i])
print()

print("From 0th position to last position")
b = x[0:]
for i in b:
    print(i)
print()

print("Last 4 Elements :")
d = x[-4:]
for i in d:
    print(i)
print()


print("Last 5 elements with [-5-(-3)]=2 element towards right :")
f = x[-5:-3]
for i in f:
    print(i)