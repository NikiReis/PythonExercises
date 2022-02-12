import random

number = random.randint(0,5)
guess = int(input("Type the number that the computer thought: "))

if guess==number:
 print("Congrats, that's the right number!")
else:
    print("Sorry!But that's not the number that the computer thought")