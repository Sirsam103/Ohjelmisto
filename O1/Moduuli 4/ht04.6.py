import random
i = int(input("Arvottavien pisteiden lukumäärä: "))
j, x, y, s = 0, 0, 0, 0
while j <= i:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 < 1:
        s += 1
    j += 1
else:
    print(4*s/j)