velocity = float(input("What was the velocity that the car has passed on the radar ? "))

if velocity <= 80:
    print("The car was into the permited range, no one traffic ticket will be applied!")
else:
    print("The car was outide of the permited range, a traffic ticket has been applied!")
    print("Max velocity: 80Km/h\nRegistered velocity: {}".format(velocity))
    traffticket = (velocity-80)*7
    print("Value of the traffic ticket: R$ {:.2f} !".format(traffticket))
