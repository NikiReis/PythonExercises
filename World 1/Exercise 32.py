print("-"*12)
print("Leap Year")
print("-"*12)
try:
    year = float(input("Type a year: "))
except ValueError:
    print('PLase, type only numeric values!')
else:
    if year % 4 == 0 and (year % 100 != 0) or year % 400 == 0:
        print("The entered year is a leap year.")
    else:
        print("The entered year it's not a leap year.")
