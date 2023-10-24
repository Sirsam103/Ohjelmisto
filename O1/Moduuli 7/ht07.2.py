nimetin = (input("Anna jokin nimi: "))
nimet, x = {nimetin}, 0
while nimetin != "":
    nimet.add(nimetin)
    if len(nimet) > x:
        print("Uusi nimi")
    else:
        print("Aiemmin syötetty nimi")
    x = len(nimet)
    nimetin = input("Anna jokin nimi: ")
for n in nimet:
    print(n)
