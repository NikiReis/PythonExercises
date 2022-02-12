print("Athlete Placement")
print("-"*17)
age = int(input("Athlet's age: "))
if age <= 9:
    print("Athlete Placement: Child")
elif age > 9 and age <= 14:
    print("Athlete Placement: Childish")
elif age > 14 and age <= 19:
    print("Athlete Placement: Junior")
elif age > 19 and age <= 25:
    print("Athlete Placement: Senior")
else:
    print("Athlete Placement: Master")
