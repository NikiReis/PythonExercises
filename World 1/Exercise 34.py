print("-"*15)
print("Salary Raise v2")
print("-"*15)

def salary_raise(salary):
    if salary <= 2150:
        new_salary = salary + (salary*0.15)
    else:
        new_salary = salary + (salary*0.10)
    print(f'The salary adjusted is: R$ {new_salary:.2f}')


try:
    salary = float(input("What's the employee salary ? "))
    if salary < 350:
        print('The lower salary in the company is U$ 350,00, please try again!')
        exit()
except ValueError:
    print('Somethin\'s wrong, please, try again!')
else:
    salary_raise(salary)
