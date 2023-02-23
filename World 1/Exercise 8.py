try:
    num = int(input('Type a distance in meters: '))
    if num < 0:
        num = abs(num)
except ValueError:
    print(f'Please type only numeric values')
else:
    print(f'Distance of {num} meters is equal to: ', end='\n')
    print(f'Kilometers: {num/1000}km\nHectometers: {num/100}hm\nDecameters: {num/10}dam', end='\n')
    print(f'Decimeters: {num*10}dm\nCentimeters: {num*100}cm\nMillimeters: {num*1000}mm')
