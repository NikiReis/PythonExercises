import random
from time import sleep

itens = ["Rock", "Paper", "Scissors"]
computer = random.choice(itens)

print("-"*24)
print("Scissors, Paper and Rock")
print("-"*24)

print("Your Options")
print("[1] Rock\n[2] Paper\n[3] Scissors")
player = int(input("Choose one option: "))
print("-"*17)

print("Scissors")
sleep(0.5)
print("Paper")
sleep(0.5)
print("Rock")
sleep(0.5)

print("-"*16)

if computer == "Rock":

    if player == 1:
        print("No one won!\nThat's a draw")
    elif player == 2:
        print("And the Winner is: Player")
    elif player == 3:
        print("And the Winner is: Computer")
    else:
        print("Invalid movement")

elif computer == "Paper":

    if player == 1:
        print("And the Winner is: Computer")
    elif player == 2:
        print("No one won!\nThat's a draw")
    elif player == 3:
        print("And the Winner is: Player")
    else:
        print("Invalid movent")

elif computer == "Scissors":
    if player == 1:
        print("And the winner is: Player")
    elif player == 2:
        print("And the Winner is: Computer")
    elif player == 3:
        print("No one won!\nThat's a draw")
    else:
        print("Invalid movement")

if player == 1:
    print("Player Choosed: Rock")
elif player == 2:
    print("Player Choosed: Paper")
else:
    print("Player Choosed: Scissors")
print("Computer Choosed: {} ".format(computer))
