'''
#create array example 1

import array
stu_roll = array.array('i', [101, 102, 103, 104, 105])
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])  
print(stu_roll[3])
print(stu_roll[4])
'''
#create array example 2
'''
import array as arr
stu_roll = arr.array('i', [101, 102, 103, 104, 105])
print(len(stu_roll))
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])  
print(stu_roll[3])
print(stu_roll[4])
'''
#create array example 3
'''
from array import *
stu_roll = array('i', [101, 102, 103, 104, 105])
print(len(stu_roll))
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])  
print(stu_roll[3])
print(stu_roll[4])
'''
#create array example 4
'''
from array import *
stu_roll = array('f', [10, 20, 10.3, 40, 1.5])
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])  
print(stu_roll[3])
print(stu_roll[4])
print(type(stu_roll))
'''
#create array example 5
from array import *
stu_roll = array('i', [101, 102, 103, 104, 105])
for element in stu_roll:
    print(element)