first = int(input("Type the first number: "))
second = int(input("Type the second number: "))

option = 0

while option != 5:
	
    print("[1] Sum the two values\n[2] Multiply")
    print("[3] Greatest\n[4] New values\n[5] Exit program")
    option = int(input("Type the disered option: "))
	
    if option ==1:
        print("The sum of the two values is equal to: {}".format(first+second))
        
    elif option == 2:
        print("The resulte of the multiplication is: {}".format(first*second))
     
    elif option == 3:
        
        if first > second:
            print("The highest is {}".format(first))
        else:
            print("The highest is {}".format(second))
            
    elif option == 4:
        first = int(input("Type the first number: "))
        second = int(input("Type the second number: "))
