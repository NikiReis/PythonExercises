from os import system, name

print("-"*26)
print("Highest and lowest weights")
print("-"*26)

highest = 0
lowest = 0

for i in range (0,5):
    weight = int(input("Type the weight: "))
    def clear():
        if name =='nt':
          _= system('clear')
    if i == 1:  
        highest = weight
        lowest = weight
    else:
        if weight > highest:
            highest = weight
        if weight < lowest:
            lowest = weight
        
print("The highest was {}kg, and the lowest was {}kg ".format(highest,lowest))
