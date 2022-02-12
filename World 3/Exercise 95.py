data = dict()
goals = list()
alldata = list()
while True:

    data.clear()
    data['Name'] = str(input("Player's name: "))
    while True:
        try:
            data['Matches'] = int(input(f"How many matches has {data['Name']} played ? "))
        except ValueError as e:
            print("Type only integers numbers!")
        else:
            break

    goals.clear()
    for x in range(0,data['Matches']):
        goals.append(int(input(f"How many goals has {data['Name']} scored in the match {x+1} ? ")))
    data['Goals'] = goals[:]
    data['Total'] = sum(goals)
    data['AVG'] = (sum(goals)/data['Matches'])
    alldata.append(data.copy())

    while True:
        answer = str(input("Do you want to register anyone else ? (Y) = Yes, (N) = No : ")).upper()
        if answer not in 'YN':
            print("Please, type only 'Y' or 'N' ")
        else:
            break
    if answer == 'N':
        break

print("-"*22)
for x in alldata:
    for k,v in x.items():
        print(f"{k} = {v}")
    print()
print("-"*22)

while True:
    search = int(input("Type the player's code that you want to research: (999 ens the research) "))
    if search == 999:
        break
    if search >= len(alldata):
        print("Error! That code owns to no one")
    else:
        print(f"Player's data: {alldata[search]['Name']}")
        for x,y in enumerate(alldata[search]['Goals']):
            print(f"In the match {x+1} he scored {y} goals")
    print("-"*22)

    print(f"The key {k} has the value: {v}")
print("-"*22)

player = str(input("Type the player's name that you want to research: "))
for x in alldata:
    if player in x['Name']:
        for k, v in x.items():
            print(f"{k}, {v}")
