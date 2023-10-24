def muunnin(litraa):
    litraa = gallonaa * 3.785
    return litraa
gallonaa = int(input("Anna bensiinin gallona määrä: "))
litraa = muunnin(gallonaa)
print(litraa)