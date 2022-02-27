import Coin

r = float(input("Price of the product: "))
print(f"Doubleded is: USD {Coin.double(r)}")
print(f"Half of the price is: USD {Coin.half(r)}")
print(f"Increasing by 10% is: USD {Coin.percent(r,10)}")
print(f"Decreasing 13% is: USD {Coin.reducing(r,13)}")