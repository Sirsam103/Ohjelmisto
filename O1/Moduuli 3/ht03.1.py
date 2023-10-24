kuha = int(input("Kuhan pituus senttimetreinä: "))
if kuha < 37:
    print("Kuhan pituus ei valitettavasti riitä.\nPalauttakaa se veteen. \nTeiltä puuttuu ", 37-kuha, "senttimetriä")
else:
    print ("Onneksi olkoon kuhan pituus täyttää vähimmäismitat")
