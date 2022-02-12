import random
print("-"*21)
print(" 'Prize Draw Part 2 '")
print("-"*21)
stdnt1 = str(input("First one: "))
stdnt2 = str(input("Second : "))
stdnt3 = str(input("Third : "))
stdnt4 = str(input("Fourth : "))
list = [stdnt1, stdnt2, stdnt3, stdnt4]
random.shuffle(list)
print("-"*21)
print("The chosen order was:\n{}".format(list))
