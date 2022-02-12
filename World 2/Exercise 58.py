from random import randint
    
computer = randint(0,10)
    
print("Guessing Number")    
print("-"*15)    
    
player = int(input("Try to guess the number that the computer thought: "))

attempt = 1

while player != computer:
    print("Sorry, you choosed the wrong number\n")
    player = int(input("Try to guess the number that the computer thought: "))
    attempt += 1
    
print("Congrats! you choosed the correct number!")
print("You needed {} attempts ".format(attempt))
