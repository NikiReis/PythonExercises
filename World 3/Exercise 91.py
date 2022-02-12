import random
from operator import itemgetter

ranking = []

alldata = {'player1':  random.randint(1,6),
            'player2': random.randint(1,6),
            'player3': random.randint(1,6),
            'player4': random.randint(1,6)}

for k,v in alldata.items():
    print(f"The {k} get: {v}")
ranking = sorted(alldata.items(), key = itemgetter(1), reverse=True)
print()
for i,v in enumerate(ranking):
    print(f"The {v[0]} was in the {i+1} place, who get the number: {v[1]} in the dice")
    print()
   
