def half(number = 0):
    r = number / 2
    return r

def double(number = 0):
    r = number * 2 
    return r

def percent(number = 0, percentage = 0):
    r = number + (number*percentage/100)
    return r

def reducing(number = 0, percentage = 0):
    r = number - (number*percentage/100) 
    return r 

def coin2(number = 0):
    return f'{number:.2f}'.replace('.',',')