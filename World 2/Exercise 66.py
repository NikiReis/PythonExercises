print("Working with Numbers")
print("-"*20)

number = total = count =0
print("999 will break the looping")

while number != 999:
    number=int(input("Type a number: "))
    if number == 999:
        break
    total += number
    count += 1     
print("Sum of the numbers: {}\nQuantity of numbers typed: {}".format(total,count))
