# #to create a dictionary
d = dict()
# # print(type(d))
d = dict(
    {
        100:'sonu',
        102:'mohan',
        103:'anuj'
    }
)
print(d)

d = dict([(100,"sonu"),(200,"shiva"),(300,"ravi")])
print(d)

print(len(d))


#get function
d = {
    101:'sonu',
    102:'anil',
    103:'karan',
    104:'pankaj',
    105:'mohan'
}
print(d[101])
# print(d[106])

print(d.get(101))
print(d.get(106))

print(d.get(101,"guest"))

print(d.get(600,"guest"))

#pop () function
d = {
    100:"sunil",
    101:"ravi",
    102:"shiva"
}
print(d)
print()
print(d.pop(100))
print(d)
print()
print(d.pop(400))

#popitem () function
d = {
    100:"sunil",
    200:"ravi",
    300:"shiva"
}

print(d)
print()
print(d.popitem())
print(d)

d = {}
print(d.popitem()) #KeyError: 'popitem(): dictionary is empty'


# #keys() function
d = {
    100:"sunil",
    200:"ravi",
    300:"shiva"
}

print(d.keys())
for k in d.keys():
    print(k)

print()
print()
# #values() function
d = {
    100:"sunil",
    200:"ravi",
    300:"shiva"
}

print(d.values())
for k in d.values():
    print(k)

#setdefault() function
d = {
    100:'sunil',
    200:'ravi'
}
print(d.setdefault(400,'pavan'))
print(d)
print(d.setdefault(100,'sunil'))
print(d)

#update() function
# #write a progam to take dictionary from the keyboard and print the sum of values ?
d = eval(input("Enter Dictionary : "))
s = sum(d.values())
print("Sum =",s)

#writeb a program to accept student name and marks from the keyboard and creates a dictionary.  Also display marks by taking student name as input ?

n = int(input("Enter the number of students :"))
d = {}
for i in range(n):
    name = input("Enter student Name :")
    marks = input("Enter Student Marks :")
    d[name] = marks
while True :
    name = input("Enter student Name to get Marks :")
    marks = d.get(name,-1)
    if marks == -1:
        print("Student not Found !")
    else:
        print("The Marks of",name,"are",marks)
    option = input("Do you want to find another student marks [Yes | No]")
    if option == "No":
        break
print("Thanks for using our application !")




