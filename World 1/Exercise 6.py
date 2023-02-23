import math
def math_ops(value):
    if value < 0:
        return f'Number: {value}\nDouble: {value * 2}\nTriple: {value * 3}\nSquare root: Numeric values doesn\'t have square roots!!'
    else:
        return f'Number: {value}\nDouble: {value * 2}\nTriple: {value * 3}\nSquare root: {math.sqrt(value):.3f}'


try:
    number = float(input('Type a value: '))
except ValueError:
    print('Invalid value. Please, type only numeric values!! ')
else:
    print(math_ops(number))
