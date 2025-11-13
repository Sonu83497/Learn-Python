num = int(25.5)
print("The integer value is:", num)
print("Type of the value is:", type(num))
print(float(num))

t = int(True)
print("The integer value of True is:", t)

t = int(False)
print("The integer value of True is:", t)

n = int("100")
print("The integer value from string is:", n)

n = int("100.5")  # This will raise a ValueError
print("The integer value from string is:", n)