import os
number = highest = lowest = 0
summ = 0
resp = ''
count = 0
average = 0

while resp != 'NO':
    highest = number
    lowest = number

    number = int(input("Type a value: "))
    if number > highest:
        highest = number
    elif number < lowest:
        lowest = number
    summ += number

    print("Press any bottom to continue\nOr press 'No' to split up")
    resp = str(input("You want to continue ? ")).upper()
    count += 1
    os.system('cls' if os.name == 'nt' else 'clear')

average = summ/count.__trunc__()
print("Lowest number: {}\nHighest number : {}\nAverage: {}".format(
    lowest, highest, average))
