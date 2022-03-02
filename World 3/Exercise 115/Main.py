from Exercise_115.Interface import *
from Exercise_115.Functions import *

data_base = 'registers.txt'

while True:
    screen()
    options = menu('Type a value: ')
    print(line())

    if options == 1:

        if validation_file(data_base) == True:
            name = str(input('Type the name: '))
            age = validation_number('Type the age: ')
            registering(data_base,name,age)
        else:
            create(data_base)
            mensagem()
            name = str(input('Type the name: '))
            age = validation_number('Type your age: ')
            registering(data_base,name,age)

    elif options == 2:
        search(data_base)
    elif options == 3:
        print("Ok... Thanks for using our sistem, come back soon!")
        break
    else:
        print('Invalid Option')
