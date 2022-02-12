import os

total = totalthousand = lowest = count = 0
cheapestname = ''

while True:

    product = str(input("Type the product's name: "))
    price = int(input("Type the value of the product USD: "))
    count += 1
    total += price

    if price >= 1000:
       totalthousand += 1  
    if count == 1 or price < lowest:
        lowest = price
        cheapestname = product

    answer = ' '
    
    while answer not in 'YN':
        answer = str(input("Do you want to continue: \'Y\' (Yes) - \'N\' (No): ")).upper()

    if answer == 'N':
        break

os.system('cls' if os.name=='nt' else 'clear')
print(f"Total value of the bought: USD {total:.2f}")
print(f"We have {totalthousand} product(s) that coast more or equal to USD 1.000,00")
print(f"The cheapest product coast USD {lowest:.2f} and it's the: {cheapestname}")