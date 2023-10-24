i = 0
while i <=4:
    k = input("Käyttäjätunnus: ")
    s = input("Salasana: ")
    if k == "python":
        if s == "rules":
            print("Tervetuloa")
            break
        else:
            print("")
    else:
        print("")

    i += 1
else:
    print("Pääsy evätty")