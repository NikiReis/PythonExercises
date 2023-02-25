frase = str(input("Write a sentence: ")).upper().strip()
print("The letter 'A' and 'a' shows up {} times".format(frase.count("A")))
print("The first letter 'A' shows up in {} position".format(frase.find("A")+1))
print("The last letter 'A' shows up in the {} position".format(frase.rfind("A")))

