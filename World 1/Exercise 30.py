def odds_evens(number):
    if number % 2 == 0:
        print("The typed value is a even number")
    else:
        print("The typed value is a odd number")


try:
    intvalue = int(input("Type a number: "))
except ValueError:
    print('PLease, type only numeric values!!')
else:
    odds_evens(intvalue)
