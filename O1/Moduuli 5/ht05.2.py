numerot = []
numero = input("Anna jokin luku, lopettaaksesi paina enter: ")
while numero != "":
    numerot.append(numero)
    numero = input("Anna jokin luku, lopettaaksesi paina enter: ")
numerot.sort(reverse=True, key=int)
print(numerot[0:5])
