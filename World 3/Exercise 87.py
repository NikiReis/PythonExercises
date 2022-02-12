arrays = [[0,0,0],[0,0,0],[0,0,0]]
sumevens = 0
higher = 0
sumofy = 0

for x in range(0,3):
    for y in range(0,3):
        arrays[x][y] = int(input(f"Type a valeu to put at the position [{x}][{y}] in the arrays: "))
        if arrays[x][y] % 2 == 0:
            sumevens += arrays[x][y]

## catch the higher value of the second line 
for y in range(0,3):
    if y == 0:
        higher = arrays[1][y]
    elif arrays[1][y] > higher:
        higher = arrays[1][y]

## sum the value of the third column
for x in range(0,3):
    sumofy += arrays[x][2]



## print the array
for x in range(0,3):
    for y in range(0,3):
        print(f"[{arrays[x][y]:^3}]",end='')
    print()
## print some equations
print(sumofy) ## print the sum of the third column
print(sumevens) ## print the sum of all evens
print(higher) ## print the higher value at in the second line
