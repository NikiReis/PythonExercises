array = [[0,0,0],[0,0,0],[0,0,0]]

for x in range (0,3):
    for y in range (0,3):
        array[x][y] = int(input(f"Type a value to put o the position: {[x]},{[y]}: "))
for x in range (0,3):
    for y in range (0,3):
        print(f'[{array[x][y]:^3}]',end='')
    print()
