from random import randint
numbers = randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)
print(f"Sorted Numbers:")
for c in numbers:
    print(f"{c} ",end='')
print(f"\nHigher value sorted: {max(numbers)}")
print(f"Lowest value sorted: {min(numbers)}")
