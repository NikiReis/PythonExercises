print("-"*21)
print("    School Average   ")
print("-"*21)
name = str(input("Name of the student:"))
note1 = float(input("First note: "))
note2 = float(input("Second note: "))
average = (note1+note2)/2
print("The average of the {} was : {} points".format(name,average))