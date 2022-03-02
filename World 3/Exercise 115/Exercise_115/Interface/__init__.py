def validation_number(num):
    while True:
        try:
            value = int(input(num))
        except (ValueError, TypeError):
            print("Error!Please, enter a valid valued")
        except KeyboardInterrupt:
            print("Ok... Thanks for using our sistem, come back soon!")
            break
        else:
            return value


def line(lenght=42):
    return '-' * lenght


def screen():
    print(line())
    print('Registration Menu'.center(42))
    print(line())


def menu(liist):
    print('1 - Register a Person')
    print('2 - List All Registered People')
    print('3 - Exit The Sistem')
    option = validation_number(liist)
    return option
