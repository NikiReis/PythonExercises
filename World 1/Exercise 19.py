from random import choice

try:
    print('Prize Draw')
    quantity = int(input('How many students does the classroom has ? '))
except ValueError:
    print('Error! Type only numeric numbers!')
else:
    students = []
    for x in range(0, quantity):
        students.append(str(input(f'Type the name of the {x} student: ')))
    print(f'The chosen one was: {choice(students)}')
