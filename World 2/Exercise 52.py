value = int(input("Type a value: "))
count = 0

for a in range(1, value+1):
    if value % a == 0:
        count += 1
print("-"*31)
print("The number was divisible {} time".format(count))
print("-"*31)
for a in range(1, value+1):
    if value % a == 0:
        print("{}".format(a), end=" ")
if count != 2:
    print("\nSo, the number '{}' isn't a prime number".format(value))
else:
    print("\nThe number '{}' is a prime number".format(value))
