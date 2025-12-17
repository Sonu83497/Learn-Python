from time import time, ctime, localtime
# Time  = time()
# print("Epoch second :",Time)
# print()
# et = ctime(Time)
# print("Epoch date and time :",et)
# print()
# ct = ctime()
# print("Current Time :",ct)


# print()

# epoch = time()
# print(epoch)
# print("Epoch time in second",epoch)
# et = ctime(epoch)
# print("Epoch Date and time :",et)
# print()


ct = ctime()
print("Current Date and time :",ctime())
print()

stobj = localtime()
print("struct_time object: ",stobj)
print()

print("Year :", stobj.tm_year)
print("Month :", stobj.tm_mon)
print("Date :", stobj.tm_mday)
print("Hour :", stobj.tm_hour)
print("Minute :", stobj.tm_min)
print("Second :", stobj.tm_sec)
print()

print(stobj.tm_mday,end="/")
print( stobj.tm_mon,end="/")
print( stobj.tm_year)
print( stobj.tm_hour,end=":")
print( stobj.tm_min,end=":")
print( stobj.tm_sec)
print()










