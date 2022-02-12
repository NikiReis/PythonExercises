def fatorial(value,show=False):
    """
    def fatorial -> Reest a input value to the user
    parâmetro 1 -> - n - is passed to the parameter 'value' to be calculated 
    parâmetro 2 -> - OPTIONAL - will show in the screeen - or not - the factorial calculation step by step
    output -> Return the result of the calculation with the funcion -> 'return'
    """
    total = 1

    for c in range(value,0,-1):
        if show:
            print(c,end='')
            if c > 1:
                print(" x ",end='')
            else:
                print(" = ",end='')
        total *=c 
    return total
    
n = int(input("Type a value to calculate factorial: "))
print(fatorial(n,show=True))
