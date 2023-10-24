numero = int(input("Anna jokin luku: "))
onko = "on"
for j in range(2, numero):
    if numero % j == 0 and (j != 1 or j != numero):
        onko = "ei ole"
        #print(j, " -läpi")
        break
print(f"Numero {numero} {onko} alkuluku")