def city_analysis(city_name):
    print("City Analysis")
    print("Your city has 'Saint' at start of the name ? ")
    print(city_name[:5].upper() == 'Saint')


try:
    city = str(input("Write the name of you city: ")).strip()
    if city.isnumeric():
        print('Please, don\'t type numbers, numbers can\'t be accept')
        exit()
except ValueError:
    print('Somethin\'s wrong, please try again')
else:
    city_analysis(city)
