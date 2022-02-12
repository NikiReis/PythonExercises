from math import sqrt
opposite = float(input("Type the opposite side of the triangle rectangle: "))
adjside = float(input("Now type the adjacent side: "))
hypotenuse = sqrt((opposite**2)+(adjside**2))
print("The hypetonuse of this triangle is equivalent to: {:.2f}".format(hypotenuse))
