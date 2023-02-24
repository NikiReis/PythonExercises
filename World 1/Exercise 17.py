def triangle_hypotenuse(opposite, adjacent):
    from math import hypot
    hypotenuse = hypot(opposite, adjacent)
    return f'{hypotenuse:.4f}'


try:
    number1 = float(input('Type the measure of the opposite triangle: '))
    number2 = float(input('Type the measure of adjacent side of the triangle: '))
except ValueError:
    print('Please, type only numeric values: ')
else:
    print(triangle_hypotenuse(number1, number2))

