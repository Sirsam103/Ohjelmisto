lentoasemat = {"EFHK": "Helsinki-Vantaan lentoasema"}
while True:
    toim = input("Mikäli haluat etsiä lentokenttää listasta, niin paina (E) ja enter\n"
                 "Mikäli haluat lisätä lentokentän listaan, niin paina (L) ja enter\n"
                 "Mikäli haluat lopettaa, niin paina enter\n")
    if toim == "":
        break
    elif toim.lower() == "l":
        ICAOk = input("Anna lentokentän ICAO koodi: ")
        lentok = input("Syötä lentokentän nimi: ")
        lentoasemat[ICAOk] = lentok
    elif toim.lower() == "e":
        ICAOk = input("Anna lentokentän ICAO koodi: ")
        if ICAOk in lentoasemat:
            print(f"ICAO koodilla: {ICAOk} löytyi {lentoasemat[ICAOk]}.\n")
        else:
            print("Tällä ICAO koodilla ei löytynyt lentoasemaa.")
            lisaa = input("Mikäli haluat lisätä sen, niin paina (L) ja enter\n"
                          "Mikäli haluat jatkaa, niin paina enter\n")
            if lisaa.lower() == "l":
                lentok = input("Syötä lentokentän nimi: ")
                lentoasemat[ICAOk] = lentok