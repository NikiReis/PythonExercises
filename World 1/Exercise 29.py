def speed_check(speed):
    if speed <= 80:
        print('The car was under the permitted range, a fine wasn\'t applied ')
    else:
        print('Car\'s speed was higher than the legal range of speed, a fine has been applied')
        return f'Fine\'s value U$ {(speed-80)*7.37:.2f}'


try:
    velocity = float(input("What was the velocity that the car has passed on the radar ? "))
    if velocity <= 0:
        print('The speed can\'t be 0 or negative, otherwise you didn\'t pass through the speed tracker')
        exit()
except ValueError:
    print('Please, type only numeric values, strings can\'t be accept !!')
else:
    print(speed_check(velocity))
