from time import sleep
print("-"*10)
print("BRL to USD")
print("-"*10)
usd = float(input("What's the dollar's value at the moment ? "))
sleep(1)
brl = float(input("Right, how R$ do you want to convert ? "))
converted = brl/usd
print("-"*10)
print("R$ {} converted to dollar is esquivalent to: {:.2f} USD".format(brl,converted))