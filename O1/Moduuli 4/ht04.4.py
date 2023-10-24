import random
r = random.randint(1, 10)
while 1!=0:
    i = int(input("Arvaa jokin luku väliltä 1-10: "))
    if i==r:
     print("Oikein")
    elif i < r:
        print("Liian pieni, arvaa uudelleen")
    elif i > r:
        print("Liian suuri, arvaa uudelleen")