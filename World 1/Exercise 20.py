def random_order(number):
    from random import shuffle
    students = []

    for x in range(0, number):
        names = str(input(f'Type the name of the {x + 1} student: '))
        students.append(names)
    shuffle(students)

    return f'The chosen order was {students}'


try:
    print('Prize Draw')
    quantity = int(input('How many students does the classroom has ? '))
except ValueError:
    print('Error! Type only numeric numbers!')
else:
    print(random_order(quantity))
