def half(price=0, formatation=False):
    r = price / 2
    return r if formatation is False else coin2(r)


def double(price=0, formatation=False):
    r = price * 2
    return r if formatation is False else coin2(r)


def percent(price=0, percentage=0, formatation=False):
    r = price + (price*percentage/100)
    return r if formatation is False else coin2(r)


def reducing(price=0, decreased=0, formatation=False):
    r = price - (price*decreased/100)
    return r if formatation is False else coin2(r)


def coin2(price=0, valor='USD '):
    return f'{valor}{price:.2f}'.replace('.', ',')


def resume(price=0, percentage=0, decreased=5):
    print("-"*30)
    print("Resume".center(30))
    print("-"*30)
    print(f"Price: {coin2(price)}")
    print(f"Doubleded: {double(price,True)}")
    print(f"Half: {half(price,True)}")
    print(f"{percentage}% of increase: {percent(price,percentage,True)}")
    print(f"{decreased}% of decrease: {reducing(price,decreased,True)}")
    print("-"*30)
