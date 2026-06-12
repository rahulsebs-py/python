cost = float(input("Enter cost price: "))
selling = float(input("Enter selling price: "))
if selling > cost:
    print("Profit =", selling - cost)
elif cost > selling:
    print("Loss =", cost - selling)
else:
    print("Draw match!")