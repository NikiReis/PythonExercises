print("Numeric Bases Conversor: ")
number = int(input("Tap one value: "))

print("Options")
print("-"*9)
print("[1] Binary")
print("[2] Hexadecimal")
print("[3] Octagonal")
option = int(input("Write the desired option: "))

if option == 1:
    print("{} converted to Binary is equal to: {} ".format(
        number, bin(number)[2:]))
elif option == 2:
    print("{} converted to Hexadecimal is equal to: {}".format(
        number, hex(number)[2:]))
else:
    print("{} converted to Octagonal is equal to: {}".format(
        number, oct(number)[2:]))
