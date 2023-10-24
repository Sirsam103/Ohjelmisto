n = []
while True:
    i = input("Anna jokin luku: ")
    if i == "":
        break
    try:
        j = float(i)
        n.append(j)
    except ValueError:
        break
if n:
    print(f"Korkein luku on: {max(n):.0f} ja pienin luku on {min(n):.0f}")
