from time import sleep

def contador(ini,fi,pa):
    print("=-"*22)
    print(f"Counting from {ini} till {fi} \'jumping\' {pa} unity(ies) ")
    if ini > fi and pa > 0:
        pa = (pa*-1)
        fi -= 1
    if fi > ini and pa < 0:
        pa = (pa*-1)
    if fi > ini and pa > 0:
        fi += 1
    for x in range(ini,fi,pa):
        print(f"{x}",end=' ',flush=True)
        sleep(0.75)
    print("End")

contador(1,10,1)
contador(10,0,2)
print("=-"*22)
print("Now it's your turn to create a counting")
start = int(input("Type the initial number: "))
end = int(input("Type the final number: "))
jump = int(input("To reach the final number, how many unity(ies) do you want to \'jump\' ? "))
contador(start,end,jump)
