#### My solution

def readInt(): 
    n = 0
    while True:
        try:
            n = int(input("Type a numeric value: "))
        except ValueError as e:
            print("Please, enter only integer value!")
        else:
            break
    print(f"You've just entered the number: {n}")

readInt()

#### Solution showed at the class

def readInt(msg):
    ok = False
    value = 0 
    while True:
        n = str(input(msg))
        if n.isnumeric():
            value = int(n)
            ok = True 
        else:
            print("Error! Type a valid integer number: ")
        if ok:
            break
    return value

n = readInt('Type a number: ')
print(f"You've just entered the number: {n}")
