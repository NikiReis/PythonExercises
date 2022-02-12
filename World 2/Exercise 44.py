from optparse import Option


print("Payment Method and Discount")
print("-"*30)
price = float(input("Type the value of the product: R$ "))
print("-"*14)
print("Payment Method")
print("-"*14)
print("[1] Cash Payment\n[2] Check Payment\n[3] Debit Card")
print("[4] Two installments in the Credit Card\n[5] Three or more Installments in the Credit Card")
option = int(input("Choose an option: "))
if option == 1 or option == 2:
    price = price - (price*0.1)
    print("Value to be paied: R$ {}".format(price))
elif option == 3:
    price = price - (price*0.05)
    print("Value to be paied: R$ {}".format(price))
elif option == 4:
    print("Value to be paied: R$ {}".format(price))
elif option == 5:
    installments = int(input("In how many installments do you want to pay ? "))
    installmentvalue = price/installments
    newvalue = installmentvalue + (price*0.20)
    print("Installments' value: R$ {}".format(newvalue))
    print("Product's final value: R$ {}".format(newvalue*installments))
