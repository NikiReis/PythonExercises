def guessing_number(guess):
    import random
    computer_number = random.randint(0, 10)

    if guess == computer_number:
        print("Congrats, that's the right number!")
    else:
        print("Sorry! But that's not the number that the computer thought")


try:
    number = int(input('Type the number that the computer thought: '))
except ValueError:
    print('Please, type only numeric values')
else:
    guessing_number(number)
