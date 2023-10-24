v = int(input("Mikä vuosi nyt on: "))
if v % 4 != 0 or v % 100 == 0 and v % 400 != 0:
    print("Vuosi ei ole karkausvuosi")
else:
    print("Vuosi on karkausvuosi")