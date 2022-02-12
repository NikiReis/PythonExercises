print("Body Mass Index")
print("-"*24)
height = float(input("Your height in meters: "))
weight = float(input("Your weight in Kilograms: "))
bmi = (weight/(height*height))
print("-"*13)
print("Classification")
print("-"*13)

if bmi < 18.5:
    print("Underweight")
    print("BMI: {}".format(bmi))
elif bmi >= 18.5 and bmi <= 24.9:
    print("Normal Weight")
    print("BMI: {}".format(bmi))
elif bmi >= 25 and bmi <= 29.9:
    print("Overweight")
    print("BMI: {}".format(bmi))
elif bmi >= 30 and bmi <= 34.9:
    print("Obesity Grade I")
    print("BMI: {}".format(bmi))
elif bmi >= 35 and bmi <= 39.9:
    print("Obesity Grade II")
    print("BMI: {}".format(bmi))
else:
    print("Obesity Grade III or Morbid")
    print("BMI: {}".format(bmi))
