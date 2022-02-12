number = summ = count = computer = 0
import random
import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Odds or Evens")
    print("-"*13)
    number = int(input("Type a value: "))
    computer = random.randint(0,10)
    oddeven = str(input("Odds or Evens [O/E]: ")).upper()
    
    while oddeven != 'O' and oddeven != 'E':
        print("Please type 'O' to Odds or 'E' to Evens")
        oddeven = str(input("Odds or Evens [O/E]: ")).upper()
    summ = computer + number
    
    if oddeven == 'E' and summ % 2 == 0:
        count += 1
    elif oddeven == 'O' and summ % 2 == 1:
        count += 1
    else: 
        break
    
if oddeven == 'E' and summ % 2 == 1:
    print(f"You choosed {number} and the computer choosed {computer}.")
    print(f"The total is {summ} a odd number")
else:
    print(f"You choosed {number} and the computer choosed {computer}.")
    print(f"The total is {summ} a even number")
    
print("Game Over! You lose!")
print(f"You won {count} times")
