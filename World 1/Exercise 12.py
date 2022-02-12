from multiprocessing.sharedctypes import Value


print("-"*23)
print("Discount Calculator")
print("-"*23)
Value = float(input("Product's value: R$ "))
discountpercentage = int(input("Discount's percentage: "))
finalvalue = Value -(Value*(discountpercentage/100))
print("-"*23)
print("The final value with {}% off: {:.2f}".format(discountpercentage,finalvalue))
print("-"*23)