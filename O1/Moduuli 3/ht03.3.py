s = int(input("Jos olet biologinen mies kirjoita 0, jos olet biologinen nainen kirjoita 1: "))
hg = int(input("Hemoglobiini arvo (g/l): "))
if s == 0:
    if hg < 134:
        print("Hemoglobiininne on alhainen")
    elif hg >195:
        print("Hemoglobiininne on liian korkea")
    else:
        print("Hemoglobiininne on hyvä")

elif s == 1:
    if hg < 117:
        print("Hemoglobiininne on alhainen")
    elif hg > 175:
        print("Hemoglobiininne on liian korkea")
    else:
        print("Hemoglobiininne on hyvä")
