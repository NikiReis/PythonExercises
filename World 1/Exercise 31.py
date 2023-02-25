def trip_value(kilometers):

    if kilometers == 0:
        print('Apparently you rant 0 kms, so you don\'t have any bill to pay')
    elif 0 < kilometers <= 200:
        price = kms * 0.50
        print("Price to be payed out equivalent\nto quantity of the kilometers that you have driven: U$ {}".format(price))
    else:
        price = kilometers * 0.45
        print("Price to be payed out equivalent\nto quantity of the kilometers that you have driven:: U$ {}".format(price))


try:
    kms = float(input("How many kilometers did you drive ? "))
except ValueError:
    print('PLease we can\'t calculate the trip value if you\'re typing a text')
else:
    trip_value(kms)
