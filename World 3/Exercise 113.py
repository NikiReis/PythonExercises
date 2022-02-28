while True:
    try:
        a = int(input("Type a integer value: "))
    except(ValueError,TypeError):
        print("\033[31mPlease type only an integer value\033[m")
    except KeyboardInterrupt:
        print("\033[31mThe user has prefered to not enter a value\033[m") 
        a = 'The user hasn\'t entered a value'
        break
    else:
        break
while True:
    try:
        b = float(input("Type a float number: "))
    except (ValueError,TypeError):
        print("\033[31mPlease type only a float number\033[m")
    except(KeyboardInterrupt):
        print("\033[31mThe user has prefered to not enter a value\033[m")
        b = 'The user hasn\'t entered a value'
        break
    else:
        break

print(f"The integer value entered was: {a}\nand the float was: {b}")
