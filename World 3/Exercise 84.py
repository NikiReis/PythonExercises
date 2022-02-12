import os 
data = []
people = []
highest = lowest = 0
while True:
  data.append(str(input("Type the name of the person: ")))
  data.append(int(input("Type the weight of the person: ")))
  if len(people) == 0:
    highest = lowest = data[1]
  else:
     if data[1]>highest:
        highest = data[1]
     if data[1]<lowest:
        lowest = data[1]
  people.append(data[:])
  data.clear()
  answer = str(input(" You want to continue ? "))
  if answer in 'NoNOn':
    break
os.system('cls' if os.name == 'nt' else 'clear')
print(f"The greatest weight was: {highest}Kg\nPerson or people with that weight: ",end='')
for p in people:
  if p[1] == highest:
    print(f"{p[0]}",end='')
print()
print(f"The lowest weight was: {lowest}Kg\nPerson or people with that weight: ",end='')
for p in people:
  if p[1] == lowest:
    print(f"{p[0]}",end='')
print()
print(f"Numbers of registers: {len(people)}")
