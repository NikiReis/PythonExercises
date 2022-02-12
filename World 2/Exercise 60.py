#first option 

number = int(input("Type a value to calcule the factorial: "))
count = number
position = count

while count > 1:
    count -= 1
    number = number * count
    
print("The factorial of {} is: {}".format(position,number))

#second option
      
from math import factorial

number = int(input("Type a value to calcule the factorial: "))
result = factorial(number)
print("The factorial of {} is: {}".format(number,result)) 
