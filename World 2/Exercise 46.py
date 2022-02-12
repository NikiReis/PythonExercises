import emoji
from time import sleep

print("-"*28)
print("Regressive Count to New Year")
print("-"*28)

for a in range(10, 0, -1):
    print(a)
    sleep(1)
print(emoji.emojize("Happy New Year :fireworks:"))
