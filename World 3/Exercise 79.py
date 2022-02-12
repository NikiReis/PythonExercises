# tnumbers -> typed numbers
import os
numbers = []
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    tnumbers = int(input("Type a value: "))
    if tnumbers not in numbers:
        numbers.append(tnumbers)
    else:
        print("Duplicated value! will not add at the list")
    print("Press any button to continue\nOr 'No' to end the programm")
    resp = str(input("Want to continue ? ")).upper()
    if resp == 'NO':
        break
print(f"{sorted(numbers)}")
