import random
print("-"*14)
print(" 'Prize Draw' ")
print("-"*14)
stdnt1 = str(input("First Student: "))
stdnt2 = str(input("Second Student: "))
stdnt3 = str(input("Third Student: "))
stdnt4 = str(input("Fourth Student: "))
list = [stdnt1, stdnt2, stdnt3, stdnt4]
print("The chosen one was: {}".format(random.choice(list)))
