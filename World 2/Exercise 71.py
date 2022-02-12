print("-"*29)
print("{:^29}".format("BANK"))
print("-"*29)
value = int("How many do you want withdraw ? USD ")
total = value
ballot = 50
totalballot = 0
while True:
  if total >= ballot:
    total -= ballot
    totalballot += 1
  else:
    if totalballot == 0:
      print(f"Total of {totalballot} ballots of USD {ballot}")
    if ballot == 50:
      ballot = 20
    elif ballot == 20:
      ballot = 10
    elif ballot == 10:
      ballot = 1
    totalballot = 0
    if total == 0:
      break
