from datetime import date

today = date.today().year

count = 0
count2 = 0

for i in range(0,7):
  birth = int(input("Type the year of your birthday: "))
  age = today - birth
  if age >= 21:
    count += 1
  else:
    count2 += 1
    
print("The number of people who has achieved the legal age is: {}".format(count))
print("The number of people who hasn't achieved the legal age is: {}".format(count2))
