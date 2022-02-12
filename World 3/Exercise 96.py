## Area Calculator without parameter

def area():
    print("-"*15)
    print("Area Calculator")
    print("-"*15)
    while True:
        try:
                a = float(input("Type the width in meters: "))
        except ValueError as e:
            print("Only numeric values")
        else:
            break
    while True:
        try:
            b = float(input("Type the length in meters: "))
        except ValueError as e:
            print("Only numeric values")
        else:
            break
    s = a*b
    print(f"The area {a}x{b} is: {s:.2f}m²")
area()

## Area Calculator with parameter

def area2(width,length):
    s = width*length
    print(f"According to the entered values: {width}x{length} is equal to: {s:.2f}M²")
print("-"*15)
print("Area Calculator")
print("-"*15)
while True:
    try:
        side1 = float(input("Type the width in meters: "))
    except ValueError as e:
        print("Only numeric values")
    else:
        break
while True:
    try:
        side2 = float(input("Type the length in meters: "))
    except ValueError as e:
            print("Only numeric values")
    else:
        break
area2(side1,side2)
