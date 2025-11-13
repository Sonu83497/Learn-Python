# nested while loop
i = 1
while i <= 2:
    print("Outer Loop Iteration:", i)
    j = 1
    while j <= 3:   
        print("  Inner Loop Iteration:", j)
        j = j + 1
    i = i + 1
print("Rest of the code")