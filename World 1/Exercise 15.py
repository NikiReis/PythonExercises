def hirecars(kilometers, days):
    value_day = 60
    value_km = 0.15
    print(f'Days hired: {days}\nKilometers driven: {kilometers}')
    return f'Total value to be payed: U$ {(days*value_day)+(kilometers*value_km):.2f}'


try:
    days_hired = int(input('For how many days you hired the car ? '))
    kms_run = int(input(f'How many kilometers you drove in these {days_hired} days ?'))
except ValueError:
    print('Please type only numeric values!!')
else:
    print(hirecars(kms_run, days_hired))
