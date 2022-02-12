print("Times Table")
print("-"*18)

value = int(input("Write one value: "))
print("-"*18)

while value < 0 or value > 10:
    value = int(input("Write one value: "))

for a in range(0, 11):
    print(a, "x", value, "= {}".format(a*value))
