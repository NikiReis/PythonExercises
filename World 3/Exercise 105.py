def notas(*notes, sit=False):
    report = dict()
    report['Total'] = len(notes)
    report['Highest'] = max(notes)
    report['Lowest'] = min(notes)
    report['Avg'] = sum(notes)/len(notes)

answer = notas(7.6,8.5,9,10,sit=True)
print(answer)
