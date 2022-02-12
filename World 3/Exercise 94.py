import os
data = dict()
alldata = list()
total_age = 0

while True:
    data['Name'] = str(input("Type the person's name: "))
    while True:
        try:
            data['Age'] = int(input("Type the person age: "))
        except ValueError as e:
            print("Error! Please, type only integers numbers")
        else:
            break
    total_age += data['Age']
    while True:
        data['Sex'] = str(input("Type the person's sex: ")).upper()
        if data['Sex'] in 'MW':
            break
        else:
            print("Please, type only 'W and M' W for Woman and M for Man!")
    alldata.append(data.copy())
    data.clear()  
    while True: 
        answer = str(input("Want to continue - yes (Y), no (N) - ? ")).upper()
        if answer not in 'YN':
            print("Please, type only Y or N! ")
        else:
            break
    if answer == 'N':
        break 
os.system('cls' if os.name=='nt' else 'clear')
print(f"In total {len(alldata)} people were registered")
print(f"The Average Age is: {total_age/len(alldata)}")
print("The Women are: ",end='')
for x in alldata:
    if x['Sex'] == 'W':
        print(f"[{x['Name']}]",end='')
print()
print("People which the age is higher than the average")
for x in alldata:
    print("")
    if x['Age'] > (total_age/len(alldata)):
        for k,v in x.items():
            print(f"{k} - {v}",end=' ')
