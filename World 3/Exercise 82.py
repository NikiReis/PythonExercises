import os

odds = []
evens = []
general = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    numbers=float(input("Type a value: "))
    general.append(numbers)
    if numbers % 2 == 0:
        odds.append(numbers)
    else:
        evens.append(numbers)
    if numbers < 0:
        if (numbers * -1) % 2 == 1:
            evens.pop()
        else:
            odds.pop()
        general.pop()    
        break
print(f"List of evens: {evens}")
print(f"List of Odds: {odds}")
print(f"General numbers: {general}")
