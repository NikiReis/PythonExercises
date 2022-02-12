print("-"*12)
print("Leap Year")
print("-"*12)
ano = int(input("Type a year: "))

if ano%4==0 and (ano%100!=0) or ano%400==0:
    print("The entered year is a leap year.")
else: 
    print("The entered year it's not a leap year.")