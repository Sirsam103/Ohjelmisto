v = int(input("Mikä vuosi nyt on: "))
if v % 4 == 0 and v % 100 != 0:
    print("Vuosi on karkausvuosi")
elif v % 100 == 0 and v % 400 == 0:
    print("Vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")
