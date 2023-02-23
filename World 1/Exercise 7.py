def student_avg(value1, value2):
    return f'First grade: {value1}\nSecond grade" {value2}\nAverage student\'s grade is: {(value1+value2)/2}'


try:
    num1 = float(input('Type the first grade: '))
    num2 = float(input('Type the second grade: '))
    if num1 < 0 or num2 < 0:
        print('Value out of index!! Please type a grande between 0 and 10')
        exit()
    else:
        if num1 > 10:
            num1 = 10
        if num2 > 10:
            num2 = 10
except ValueError:
    print(f'Please type only numeric values')
else:
    print(student_avg(num1, num2))
