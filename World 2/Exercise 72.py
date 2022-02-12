numbers = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
           'twelve', 'thirteen', 'fourteen', 'fiveteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
while True:
    player = int(input("Tipe a number to show: "))
    if player >= 0 and player <= 20:
        break
    print("Number not found!\nPlease type a number bertween 0 and 20")
print(f"Written number: {numbers[player-1]}")
