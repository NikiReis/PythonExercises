print("-"*27)
num = int(input("Type a value between 0 and 9999: "))
print("-"*27)
u = num // 1 % 10
d = num // 10 % 10
h = num // 100 % 10
t = num // 1000 % 10
print("Type number has: ")
print("thousands: {} ".format(t))
print("hundreds: {} ".format(h))
print("Dozens: {} ".format(d))
print("Units: {} ".format(u))
print("-"*27)
