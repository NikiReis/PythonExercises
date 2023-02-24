from math import trunc

try:
    number = float(input('Type any float number: '))
except ValueError:
    print('Error! Texts or letters is not acceptable!')
else:
    print("that number in truncated form is: {} ".format(trunc(number)))

