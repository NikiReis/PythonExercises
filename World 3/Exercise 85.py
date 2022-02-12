numbers =[[],[]]

for a in range (0,7):
    value = int(input("Type a number: "))
    if value % 2 == 0:
        numbers[0].append(value)  
    else:
        numbers[1].append(value)
numbers[0].sort(reverse=False)
numbers[1].sort(reverse=False)
print("Evens typed: ",numbers[0])
print("Odds typed: ",numbers[1])


