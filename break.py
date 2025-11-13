'''
for i in range(10):
    if i == 2:
        print("processing is enough -- please stop")
        break
    print(i)
'''
cart = [10,20,30,40,50,60,70,80,90,100]
for item in cart:
    if item >50:
        print("item is out of stock, stopping the process : ",item)
        break
    print(f"processing item: {item}")