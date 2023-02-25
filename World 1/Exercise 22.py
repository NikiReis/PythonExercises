def name_analysis(personame):
    new_name = personame
    personame = personame.split()
    return f'You name only in upper: {new_name.upper()}\nYour name only in lower: {new_name.lower()}\nYour first name has: {len(personame[0])} letters\nYour entire name has {len(new_name)-new_name.count(" ")}: letters'


try:
    name = str(input("Type your complete name: "))
    if name.isnumeric():
        print('Please, type only names, numbers aren\'t going to be accept! ')
        exit()
except ValueError or AttributeError:
    print('Somethin\'s wrong, please try again')
else:
    print(name_analysis(name))
