def tint_wall(height, width):
    return f'Your wall has {height*width:.2f}.\nTo tint this wall i\'ll need {(height*width)/2:.2f}l of ink'


try:
    h = float(input('Type the height of the wall: '))
    w = float(input('Now type the width: '))
    if h < 0 or w < 0:
        print('The values can\'t be negative!!')
        exit()
except ValueError:
    print('You probably typed a string value, please type only numeric values!!')
else:
    print(tint_wall(h, w))
