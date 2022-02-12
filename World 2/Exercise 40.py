print("Aritmetic Average")
print("-"*16)
note1 = float(input("First note: "))
note2 = float(input("second note: "))
avg = (note1 + note2)/2

if avg < 5:
    print("Sadly you were disapproved")
    print("Your average was: {} points".format(avg))

elif avg >= 5 and avg < 7:
    print("Sadly you is on recuperation\nbut you still having chances to pass")
    print("Your average was: {} points".format(avg))

elif avg >= 7:
    print("Congratulations you have passed!")
    print("Your average was: {}".format(avg))
