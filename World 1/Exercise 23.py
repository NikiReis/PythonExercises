def transforming_numbers(number):
    print(f'Number Analysis.\nThousands: {number// 1000 % 10}\nHundreds: {number // 100 % 10}', end=' ')
    print(f'\nDozens: {number // 10 % 10}\nUnits: {number // 1 % 10}')


try:
    value = int(input('Type a number: '))
except ValueError or AttributeError:
    print('Please, type only numeric values')
else:
    transforming_numbers(value)
