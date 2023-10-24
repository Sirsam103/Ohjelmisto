v = int(input("Mikä vuosi nyt on: "))
if v % 4 == 0:
    if v % 400 == 0 and v % 100 != 0:
        i = "ei ole"
    elif v % 100 != 0:
        i = "on"
    else:
        i = "ei ole"
else:
    i = "ei ole"
print(f"Vousi {i} karkausvuosi")