def new_salary(name, salary):
    return f'Employee\'s name: {name}. Salary: {salary}.\nLinek\'s new salary after a 15% of raise: {salary + (salary*0.15):.2f}'


try:
    value = float(input("What\'s the employee salary: "))
    employee_name = str(input('What\'s the employee\'s name ? '))
    if employee_name.isnumeric():
        print('Please type only letters, numbers can\'t be accept as name!')
        exit()
except ValueError:
    print('Something\'s wrong, please try again!!')
else:
    print(new_salary(employee_name, value))
