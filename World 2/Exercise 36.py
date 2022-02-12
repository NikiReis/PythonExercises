house = float(input("Type the value of the house: "))
month = int(input("How many installments ? "))
salary = float(input("Value of your salary: "))

calculation = (house/month)

if calculation > (salary * 0.30):
    print("Sorry, but  your loan wasn't accepted")
else:
    print("Congrats! your loan was approved")
