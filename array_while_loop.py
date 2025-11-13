#create array and iterate using while loop with index
from array import *
stu_roll = array('i', [101, 102, 103, 104, 105])
n = len(stu_roll)
i = 0
while i < n:
    print(i, "=", stu_roll[i])
    i = i + 1