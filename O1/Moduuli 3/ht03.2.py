hl = input("Hyttiluokkanne: ")
if hl == "LUX" or hl == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hl == "A" or hl == "a":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hl == "B" or hl == "b":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hl == "C" or hl == "c":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")