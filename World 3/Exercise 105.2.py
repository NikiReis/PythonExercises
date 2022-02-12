n = list()

def notas(notes,sit=False):
    report = dict()
    report['Total'] = len(notes)
    report['Highest'] = max(notes)
    report['Lowest'] = min(notes)
    report['Avg'] = sum(notes)/len(notes)

    return report

quant = int(input("How many notes do you want to register: "))
for c in range(0,quant):
    n.append(int(input("Type a numeric value: ")))
print(notas(n,sit=True))
