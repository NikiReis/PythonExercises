def votacao(definition):
    from datetime import date 
    age = date.today().year - definition
    if age < 16:
        print(f"Vote denied! Vote it's only permited with 16 years old!")
        print(f"Age registered: {age}")
    elif age >= 16 and age <18 or age >70:
        print(f"Vote accept! With {age} old the vote is optional!")
    else:
        print(f"Vote accept! With {age} old the vote is mandatory!")
birthyear = int(input("type your birthday's year: "))
votacao(birthyear)
