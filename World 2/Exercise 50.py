suum = 0
for a in range(0, 6):
    number = int(input("Write one value: "))
    if number % 2 == 0:
        suum = suum + number
print("The sum is {}".format(suum))
