# d = dict()
# # print(type(d))
# d[100]="sonu"
# d[200]="pankaj"
# d[300]="anuj"
# print(d)


# d = {100:'sonu',
#      200:'anil',
#      300:"kartik"}
# print(d,type(d),d[100]) #{100: 'sonu', 200: 'anil', 300: 'kartik'} <class 'dict'> sonu

#write program to enter name and percentage marks in a dictonary and display information on the screen

# rec = {}
# n = int(input("Enter no. of students :"))
# i = 1
# while i<n:
#     name = input("Enter student name : ")
#     marks = input("Enter % of marks of student :")
#     rec[name] = marks
#     i = i+1
# print("Name of student","\t","% of marks")
# for x in rec:
#     print("\t",x,"\t\t",rec[x])


#update dictionaries
# d = {1:'sonu',2:'arun'}
# print(d)
# d[1] = 'mohit'
# print(d)
# print(d[2]) 


d ={
    101:"mahak",
    102:"anam",
    103:"tanu",
    104:"kirti",
    105:"akanksha"
} 
print(d)
d[105]="sonu"
print(d)
d[101] = "mahak sharma"
print(d)

del d[105]
print(d)

d = {
    10:"sunil",
    11:"sonu",
    12:"shiv",
    13:"mohan",
    14:"kalpesh"
}
print(d)

del d[10]
print(d)

del d[14]
print(d)







