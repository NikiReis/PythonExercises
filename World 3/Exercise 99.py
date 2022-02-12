import random
numberslist =[]

def maior(num):
    highest = 0
    for x in num:
        if x > highest:
            highest = x
    print(f"The drawn numbers were: {num}")
    print(f"And the highest number was: {highest}")
    print("-="*15)
    numberslist.clear()

for x in range(0,5):
    numberslist.append(random.randint(0,10))
maior(numberslist)
for x in range(0,2):
    numberslist.append(random.randint(0,10))
maior(numberslist)
for x in range(0,8):
    numberslist.append(random.randint(0,10))
maior(numberslist)