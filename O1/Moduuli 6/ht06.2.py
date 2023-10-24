import random
def heitto(silm):
    r=random.randint(1,silm)
    return r
silm = int(input("Anna nopan suurin silmäluku: "))
while True:
    r = heitto(silm)
    print(r)
    if r == silm:
        break
