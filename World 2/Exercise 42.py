print("Forming a Triangle")
print("-"*18)
side1 = int(input("First side: "))
side2 = int(input("Second side: "))
side3 = int(input("Third side: "))

if side1 < side3 + side2 and side2 < side1 + side3 and side3 < side1 + side2:
    print("Status: It's possible to form a triangle")
    if side1 == side2 == side3:
        print("Type of that triangle: Equilateral ")
    elif side1 != side2 != side3 != side1:
        print("Type of that triangle: Isosceles")
    else:
        print("Type of that triangle: Escalene")
else:
    print("Status: It's not possible to form a triangle with the entered values!")
