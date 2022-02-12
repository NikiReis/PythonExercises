from time import sleep
def interaction():
    while True:
        sleep(1)
        print("-"*31)
        print("Search of a Function or Library")
        print("-"*31)
        choice = str(input("Type the function or library that you want search inside of the 'interative help'\nTo finish the program type 'END': "))
        if choice == 'END':
            print("Program Finished.")
            break
        else:
            sleep(1)
            help(choice)

interaction()
