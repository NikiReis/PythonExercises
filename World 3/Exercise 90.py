studentdata = {}
alldata = []
studentdata['Name'] = str(input("Type the Student's name: "))
studentdata['AVGRADE'] = float(input("Type the Average Grade of the Student: "))
if studentdata['AVGRADE'] < 5:
    studentdata['Situation'] = ("Reproved")
elif studentdata['AVGRADE'] > 5 and studentdata['AVGRADE'] < 7:
    studentdata['Situation'] = ("Recuperation")
else:
    studentdata['Situation'] = ("Aproved")
alldata.append(studentdata.copy())
for x in alldata:
    for k,v in x.items():
        print(f"The {k} is equal to: {v}")
