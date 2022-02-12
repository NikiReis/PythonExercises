import os 
print("Times Table V3.0")
print("-"*16)

while True:
    print("Type any negative value to end the program")
    number = int(input("Wich number do you want to know the times table: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    if number < 0:
        break
    for c in range (0,11):
     print(f"{number}  X  {c} = {number*c}")
    
print("Thanks to use our programme, welcome back anytime")
