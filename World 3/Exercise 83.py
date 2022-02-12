expression=str(input("Type a expression: "))
for c in range (0,len(expression)):
    if expression.count("(") == expression.count(")"):
        print("Your expression is equivalent")
        break
    else:
        print("Your expression isn't equivalent")
        break
