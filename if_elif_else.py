brand  = input("Enter your car brand: ")
if brand.lower() == "tesla":
    print("You drive an electric car!")
elif brand.lower() == "ford":
    print("You drive a classic American car!")
elif brand.lower() == "toyota":
    print("You drive a reliable car!")
elif brand.lower() == "bmw":
    print("You drive a luxury car!")
else:
    print("You drive a", brand + ".")