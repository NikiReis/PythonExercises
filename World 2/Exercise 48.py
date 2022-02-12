calculation = 0
counter = 0

for a in range(1, 501, 2):
    if a % 3 == 0:
        calculation += a
        counter += 1
print("The sum is: {}".format(calculation))
