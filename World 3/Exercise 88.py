from random import randint
guesses = list()
allgames = list()
numberofgames = int(input("How many games do you wanna do ? "))
for i in range(0,numberofgames):
    for n in range (0,6):
        drawnumber = randint(1,60)
        if drawnumber not in guesses:
            guesses.append(drawnumber)
    guesses.sort()
    allgames.append(guesses[:])
    guesses.clear()
for x in range(0,len(allgames)):
    print(f'\nGame {x+1}: {allgames[x]}')
