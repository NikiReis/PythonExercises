def angle_measurements(angle):
    from math import sin, cos, tan, radians
    print(f'Angle: {angle}°')
    return f'Sine of the angle: {sin(radians(angle)):.2f}\nCosine: {cos(radians(angle)):.2f}\nTangent: {tan(radians(angle)):.2f}'


try:
    value = int(input('Type the angle measure: '))
except ValueError:
    print('Please, type only numeric values')
else:
    print(angle_measurements(value))
