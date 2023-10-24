import random
def heitto():
    r=random.randint(1,6)
    return r

while True:
    r = heitto()
    print(r)
    if r == 6:
        break
