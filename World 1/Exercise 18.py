import math
print("-"*22)
print("Sine, Cosine & Tangent")
print("-"*22)
angle = int(input("Write an angle: "))
print("The sine is: {:.2f}\nThe Cosine is: {:.2f}\nAnd the Tangent is: {:.2f}".format(math.sin(math.radians(angle)), math.cos(math.radians(angle)), math.tan((math.radians(angle)))))
