def temperature_converter(temperature):
    return f'Celsius degree {temperature}.\nThat\'s equivalent to {(temperature*1.8)+32:.2f} Fahrenheit'


try:
    celsius = float(input('Type the temperature in Celsius to convert to Fahrenheit: '))
except ValueError:
    print('Error! Please, type only numeric values')
else:
    print(temperature_converter(celsius))
