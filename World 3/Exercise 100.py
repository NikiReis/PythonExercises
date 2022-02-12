import random
numbers = []
evens = []

def drawing():
    for x in range (0,5):
        numbers.append(random.randint(0,100))
    print(f"Drawing numbers: {numbers}")
def evensum():
    total  = 0
    for x in numbers:
        if x % 2 == 0:
            total += x
            evens.append(x)
    print(f"Sum of the even numbers: {total}")
    print(f"List of all even numbers: {evens}")

drawing()
evensum()
