products = ('Bottle','Book','Pen','Pencil','Scissors','A4 paper')
print("-"*23)
print("Vowels inside the names")
print("-"*23)
for c in products:
    print(f"\nName: {c}\nVowels: ",end='')
    for letter in c:
        if letter.lower() in 'aeiou' and "àáéíóôuú":
            print(f"{letter}",end='')
