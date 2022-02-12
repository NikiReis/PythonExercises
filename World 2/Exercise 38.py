print("Comparing two numbers")
print("-"*21)
num1 = float(input("Write the first number: "))
num2 = float(input("Write the second number: "))

if num1 > num2:
    print("The first number is higher than the second")
elif num2 > num1:
    print("The second is higher than the first one")
else:
    print("There's no greater number, they're equivalent")
