# write a program to print right angle triangle pattern using nested loops
'''
| Step | i (Outer Loop) | j (Inner Loop) | Output Row |
| ---- | -------------- | -------------- | ---------- |
| 1    | 1              | 1              | *          |
| 2    | 2              | 1,2            | * *        |
| 3    | 3              | 1,2,3          | * * *      |
| 4    | 4              | 1,2,3,4        | * * * *    |
| 5    | 5              | 1,2,3,4,5      | * * * * *  |

#code starts here

n = int(input("Enter a number of rows:"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print() 
''' 

'''
# using while loop
| Step | i (Outer Loop) | j (Inner Loop) | Output Row          |
| ---- | -------------- | -------------- | ------------------- |
| 1    | 1              | 1              | *                   |
| 2    | 2              | 1, 2           | * *                 |
| 3    | 3              | 1, 2, 3        | * * *               |
| 4    | 4              | 1, 2, 3, 4     | * * * *             |
| 5    | 5              | 1, 2, 3, 4, 5  | * * * * *           |
| ...  | ...            | ...            | ...                 |
| 10   | 10             | 1 to 10        | * * * * * * * * * * |
#code starts here
i  = 1
while i <= 10:
    j = 1
    while j <= i:
        print("*", end=" ")
        j = j + 1
    print()
    i = i + 1 
'''

'''
| Step | Value of `i` (Outer Loop) | Value of `j` (Inner Loop) | Numbers Printed in that Row | Output After This Step                    |
| ---- | ------------------------- | ------------------------- | --------------------------- | ----------------------------------------- |
| 1    | 1                         | 1                         | 1                           | 1                                         |
| 2    | 2                         | 1, 2                      | 1 2                         | 1<br>1 2                                  |
| 3    | 3                         | 1, 2, 3                   | 1 2 3                       | 1<br>1 2<br>1 2 3                         |
| 4    | 4                         | 1, 2, 3, 4                | 1 2 3 4                     | 1<br>1 2<br>1 2 3<br>1 2 3 4              |
| 5    | 5                         | 1, 2, 3, 4, 5             | 1 2 3 4 5                   | 1<br>1 2<br>1 2 3<br>1 2 3 4<br>1 2 3 4 5 |

#code starts here
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end=" ")
        j = j + 1
    print()
    i = i + 1
'''
