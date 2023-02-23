def conversion(brl,dollar):
    return f'{brl} converted to usd dollar is equivalent to: U$ {brl/dollar:.2f}'


try:
    num = int(input('Type a value in Brl: '))
    usd = float(input("What's the value of the dollar today ? "))
    if num < 0 or usd < 0:
        print('None of the values can\'t be negative, please try again')
        exit()
except ValueError:
    print('Invalid Value! Please, type only numeric values')
else:
    print(conversion(num, usd))
