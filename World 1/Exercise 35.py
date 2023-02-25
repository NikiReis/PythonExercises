print("-"*21)
print("Forming a triangle")
print("-"*21)

try:
    side1 = float(input("Type the first side: "))
    side2 = float(input("Type the second side: "))
    side3 = float(input("Type the third side: "))
except ValueError:
    print('You probably typed a text, please try again')
else:
    if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
        print("According to the sides entered\nis possible to form a triangle!")
    else:
        print("According to the sides entered\nit's not possible to form a triangle!")
