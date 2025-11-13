name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print("Hello", name + ", you are eligible to vote.")
else:
    print("Hello", name + ", you are not eligible to vote yet.")