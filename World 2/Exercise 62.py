print("Arithmetic Progression V3.0")
print("-"*27)
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
c = 1
total = 0
plus = 10

while plus != 0:
    total = total + plus
    while c < total:
        print(num1)
        num1 = num1 + num2
        c +=1
    plus = int(input("How many you want to show ? "))
print("End")
