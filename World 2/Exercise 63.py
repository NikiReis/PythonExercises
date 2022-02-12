print("Fibonacci Sequence")
print("-"*18)
quantity=int(input("How many terms you want to show ? "))
c = 0
num1 = 0
num2 = 1
num3 = 0
print(num1,num2)
while c < quantity:
    num3 = num1 + num2
    print(num3)
    num1 = num2
    num2 = num3
    c += 1
