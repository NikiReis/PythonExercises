listnumbers = []

for c in range(0, 5):
    numbers = int(input("Type a value: "))
    if c == 0 or numbers > listnumbers[-1]:
        listnumbers.append(numbers)
    else:
        pos = 0
        while pos < len(listnumbers):
            if numbers <= listnumbers[pos]:
                listnumbers.insert(pos, numbers)
                break
            pos += 1
print(f"Typed values in order: {listnumbers}")
