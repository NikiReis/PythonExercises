print("Highest and Lowest values")
print("-"*18)

def checking_values(number1, number2, number3):
    highest = int
    lowest = int
    if number1 > number2 > number3:
        highest = number1
    elif number2 > number1 and number2 > number3:
        highest = number2
    elif number3 > number2 and number3 > number1:
        highest = number3

    if number1 < number2 and number1 < number3:
        lowest = number1
    elif number2 < number1 and number2 < number3:
        lowest = number2
    elif number3 < number1 and number3 < number2:
        lowest = number3
    print("The highest is: {}\nAnd the lowest: {} ".format(highest, lowest))


try:
    number1 = float(input("Type the first value: "))
    number2 = float(input("Type the second value: "))
    number3 = float(input("And type the third: "))
except ValueError:
    print('You probably typed a text, please try again')
else:
    checking_values(number1, number2, number3)
