def half(price=0):
    r = price / 2
    return r 


def double(price=0):
    r = price * 2 
    return r 


def percent(price=0, percentage=0):
    r = price + (price*percentage/100)
    return r 


def reducing(price=0, percentage=0):
    r = price - (price*percentage/100) 
    return r 


def coin2(price=0, valor='USD '):
    return f'{valor}{price:.2f}'.replace('.', ',')
  
  """
  The exercise 109.py didn't work in Python 3.10
  but is basically the same thing of the exercise 108.py
  """
