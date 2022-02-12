numbers = (int(input("Type a value: ")),int(input("Type another value: ")),int(input("Another one: ")),int(input("The last one: ")))
print(f"You typed the values: {numbers} ",end='')
print(f"\nThe number '9' apears: {numbers.count(9)} times")
if 3 in numbers:
    print(f"The number '3' apears in {numbers.index(3)+1} position")
else:
    print("The number '3' wasn't typed")
for n in numbers:
    if n % 2 == 0:
        print(f"Even numbers: {n}",end='')
