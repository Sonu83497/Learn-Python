# a = {10,20,30,'sonu',40,50}
# print(type(a))

# d = set()
# print(type(d))

# #accessing set using for loop
# #creating set with element
# a = {10,20,30,'sonu',40}
# for i in a:
#     print(i)

# print(type(a))

# print()
# l = [10,20,30,40,10,20,10]
# s = set(l)
# print(s)
# print(type(s))

# print()
# s = set(range(11))
# print(s)

# print()
# s = set()
# print(s)
# print(type(s))

# #Add items in given set
# s ={10,20,30}
# s.add(40)
# s.add(50)
# print(s) 

# print()

# s = {11,20,30}
# s.add(100)
# # s.add(1,2,3)
# # s.update(1)
# s.update(range(1,10,2),range(0,10,2))
# print(s)

# l = [40,50,60,10]
# s.update(1,range(5))
# print(s)  #'int' object is not iterable


# #copy set
# s1 = {10,20,30}
# s2 = s1.copy()
# print(s2)


# #pop item from set
# s = {10,20,30,40,50}
# print(s)
# print(s.pop())
# print(s)

# print()

# #remove item from set
# s = {10,20,30,40,50}
# s.remove(30)
# print(s)

# discard item from set
s = {10,20,30}
s.discard(10)
print(s)
s.discard(100)  # no error
print(s)

print()
#clear 
s = {10,20,30}
print(s)
s.clear()
print(s)