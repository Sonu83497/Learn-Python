#opening file
f = open('student.txt',mode='r')
print(f)

# closing files
# f.close()

print("File name : ",f.name)  # find file name
print("File Mode : ",f.mode)  # check file mode (read, write)
print("File closed : ",f.closed)  # checked file closed not closed
print("File readable : ",f.readable())  #Check file radable form   
print("File writable : ",f.writable())  # check file writable form 
f.close()  # file closed 
print("File closed : ",f.closed)  # checked file closed 