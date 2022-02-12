print("-"*15)
print("Salary Adjustment v2")
print("-"*15)

salary = float(input("What's the employe salary ? "))

if salary>1250:
    newsalary = salary + (salary*0.15)
else:
    newsalary = salary + (salary*0.10)
print("The salary adjusted is: R$ {}".format(newsalary))