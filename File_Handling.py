# lst = []
# for i in range (4):
#     name = input("Enter Name :")
    
#     lst.append(name)
# for i in lst:
#     print(i)
# lst = []
# for i in lst:
#     print(i)
    
# How to create a file
f = open('student.txt', mode='w')
f.write("Hello\n")
f.write('Craw Cyber Security \n')
f.write('How are you there')
f.close()
print("Writting Success")

#example :
#write the data from list to file
places = []
for i in range (4):
    name =input("Enter Name :")
    places.append(name)
with open('listfile.txt','w')as filehandle:
    for listitem in places:
        filehandle.write("%s\n" %listitem)
        
#read the data from list to file 

places = []
with open('listfile.txt','r')as filehandle:
    filecontents = filehandle.readlines()
    for line in filecontents :
        current_place = line[:-1]
        places.append(current_place)
print(places)    