import Coin

r = float(input("Price of the product: "))
print(f"USD {Coin.coin2(r)} Doubleded is: USD {Coin.double(r)}")
print(f"Half of USD {Coin.coin2(r)} , is: USD {Coin.half(r)}")
print(f"{Coin.coin2(r)} Increased by 10% is: USD {Coin.percent(r,10)}")
print(f"{Coin.coin2(r)} Decreased by 13% is: USD {Coin.reducing(r,13)}")
