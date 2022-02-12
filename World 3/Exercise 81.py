import os
list = []

while True:
    list.append(int(input("Type a value: ")))
    answer = str(input("You want to continue ? ")).upper()
    if answer in 'NO':
        break
os.system('cls' if os.name == 'nt' else 'clear')
if 5 in list:
    print(f"The number 5 was found in the {list.index(5)+1} position")
else:
    print("The number 5 wasn't found on the list")
list.sort(reverse=True)
print(f"The values in decreasing order is: {list}")
print(f"The list has: {len(list)} elements")
