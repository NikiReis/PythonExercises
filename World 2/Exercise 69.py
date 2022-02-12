resp = genre = ''
age = womancount = agecount = mancount = 0
while True:
    print("-"*17)
    print("Register a person")
    print("-"*17)
    age = int(input("Age: "))
    genre = str(input("Woman / Man [W/M]:  ")).upper()
    while genre != "W" and genre != "M":
        print("Please tipe 'W' to select woman or tipe 'M' to select man")
        genre = str(input("Woman / Man [W/M]:  ")).upper()
    if age > 18:
        agecount += 1
    if genre == 'M':
        mancount += 1
    if genre == 'W' and age < 20:
        womancount += 1
    print("Press any button to continue\nOr type 'No' to end the program")
    resp = str(input("You want to continue ? ")).upper()
    if resp == 'NO':
        break
print(f"Number of person with age higher than 18: {agecount}")     
print(f"Quantity of men's: {mancount}")
print(f"women's with less than 20: {womancount}")
