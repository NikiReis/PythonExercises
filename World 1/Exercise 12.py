def discount(value):
    if value == 0:
        print('The product\'s price is zero, that means that the product is free')
        exit()
    else:
        return f'The product that coasted U$ {value}, now with 5% of discount is costing: U$ {value - (value*0.05):.2f}'


try:
    price = float(input('How much is the product ? '))
    if price < 0:
        print('Doesn\'t exist negative prices')
        exit()
except ValueError:
    print('Please, type only numeric values!')
else:
    print(discount(price))
