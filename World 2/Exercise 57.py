
print("Genre Selection")
print("-"*15)
print("F -  Feminine\nM - Masculine")
genre = str(input("Choose the desired genre: ")).upper()

while genre != 'F' and genre != 'M':
    genre = str(input("Choose the desired genre: "))

print("The choosen was: {}".format(genre))
