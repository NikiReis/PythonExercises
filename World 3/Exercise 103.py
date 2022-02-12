def ficha(name='<<unknown>>',goal=0):
    print(f"The player {name} has scored {goal} goal(s).")


n = str(input("Player's name: "))
g = str(input("Scored Goals: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(goal=g)
else:
    ficha(n,g)
