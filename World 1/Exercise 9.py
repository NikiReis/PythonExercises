def multiplication_table(number):
    print(f'The times table of {number} is: ')
    for i in range(0, 10 + 1):
        print(f'{i} x {number}: {i * number}')


try:
    num = int(input('Type a value: '))
except ValueError:
    print('Invalid Value! Please, type only numeric values')
else:
    multiplication_table(num)