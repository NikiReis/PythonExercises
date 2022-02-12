print("Brazilian Military Army Enlistment")
print("-"*34)

age = int(input("Digite a sua idade:"))

if age == 18:
    print("Great! you're in the rigth time to do your elistment!\nPlease to go the nearest recruiting station!")
elif age > 18:
    print("You've passed {} years from the rigth time of doing your enlistment".format(age-18))
    print("Please to go the nearest recruiting station\nto update your situation with the military service.")
else:
    print("You're not in the rigth time to do your enlistment, it still remains {} years".format(18-age))
