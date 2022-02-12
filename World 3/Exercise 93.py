data = dict()
goals = list()

data['Name'] = str(input("Player's name: "))
matches = int(input(f"How many matches {data['Name']} has played ? "))

for x in range(0,matches):
   goals.append(int(input(f"How many goals {data['Name']} has scored at the match {x+1} ? ")))
data['Goals'] = goals
data['Total'] = sum(goals)
avg = (sum(goals)/matches)

print("-"*22)
print(data)
print("-"*22)

for k,v in data.items():
    print(f"The key {k} has the value: {v}")
print("-"*22)

print(f"The player {data['Name']} has played {matches} matches")
for x in range (0,matches):
    print(f"In the match {x+1} he has scored {data['Goals'][x]} goal(s)")
print(f"That means an average of {avg:.2f} scored goals per match")
