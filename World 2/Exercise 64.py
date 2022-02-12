## option 1 ---
print("Working with Numbers")
print("-"*20)

number = 0
total = 0
count = 0

while number != 999:
    number=int(input("Type a number: "))
    total += number
    count += 1 
    if number == 999:
        total -= 999
        count -= 1
print("Sum of the numbers: {}\nQuantity of numbers typed: {}".format(total,count))

## option 2 ---
print("Working with Numbers")
print("-"*20)

number = count = total = 0
number=int(input("Type a number: "))

while number != 999:
    total += number
    count += 1 
    number=int(input("Type a number: "))
print("Sum of the numbers: {}\nQuantity of numbers typed: {}".format(total,count))

## option 3 ---
print("Working with Numbers")
print("-"*20)

number = total = count =0

while number != 999:
    number=int(input("Type a number: "))
    if number == 999:
        break
    total += number
    count += 1     
print("Sum of the numbers: {}\nQuantity of numbers typed: {}".format(total,count))
