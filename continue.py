# To print oddd number in the range 0 to 9
n1  = int(input("Enter the starting number: "))
for i in range(n1):
    if i % 2 != 0:
        continue
    print(i)
    
cart = [10,20,30,40,500,600,70,80,90,100]
for item in cart:
    if item >=500:
        print("item is too expensive, skipping the item : ",item)
        continue
    print(f"processing item: {item}")