import os
alldata = list()
studentdata = list()

## collect the students data

while True:

    name = str(input("Type the name of the student: "))
    note1 = int(input("Type the first note: "))
    note2 = int(input("type the second note: "))
    studentdata.append(name)
    studentdata.append(note1) 
    studentdata.append(note2)
    studentdata.append((note1+note2)/2)
    alldata.append(studentdata[:])
    studentdata.clear()

    answer = str(input("Want to continue ? (type 0 to end): "))
    if '0' in answer:
        break
        
## show all the data registered

os.system('cls' if os.name == 'nt' else 'clear')
for x in range (0,len(alldata)):
    print(f'Number {x+1}')
    print(f'Name: {alldata[x][0]}')
    print(f'Average Grade: {alldata[x][3]}')
    print('-'*16)
    print()
    
## Ask to the user if he want to see the data of someone in especific

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    answer2 = str(input('Do you want show the notes of wich student ? '))
    for x in range (0,len(alldata)):
        if answer2 in alldata[x]:
            print(f'First Note: {alldata[x][1]}')
            print(f'Second Note: {alldata[x][2]}')
            print(f'Average Grade: {alldata[x][3]}')
    answer3 = str(input("Do you want to show the note of somebody else (press 0 to end the program) ? "))
    
    if '0' in answer3:
        break
print("Thanks for using our software! :) ")
