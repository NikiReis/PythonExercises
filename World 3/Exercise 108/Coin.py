def half(price = 0):
    r = price / 2
    return r

def double(price = 0):
    r = price * 2 
    return r

def percent(price = 0, percentage = 0):
    r = price + (price*percentage/100)
    return r

def reducing(price = 0, percentage = 0):
    r = price - (price*percentage/100) 
    return r 

def coin2(price = 0, value = 'USD '):
    return f'{value}{price:.2f}'.replace('.',',')
