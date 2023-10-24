import random
i = int(input("Arvottavien arpakuutioiden lukumäärä: "))
x = 0
for j in range(i):
    r = random.randint(1,6)
    x += r
print(f"Heittojen yhteenlaskettu summa on: {x}")