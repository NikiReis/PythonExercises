print("-"*14)
print("Km's Calculation")
print("-"*14)

kms = int(input("How many kilometers did you drive ? "))

if kms<=200:
    price = kms*0.50
    print("Price to be paied out equivalent\nto quantity of the kilometers that you have driven: R$ {}".format(price))
else:
    price = kms*0.45
    print("Price to be paied out equivalent\nto quantity of the kilometers that you have driven:: R$ {}".format(price))