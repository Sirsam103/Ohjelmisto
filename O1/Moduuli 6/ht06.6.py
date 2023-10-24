import math
def pizzahinta(pizza, hinta):
    pizhin = hinta/(math.pi * (pizza / 2) ** 2)
    #print(f"{pizhin} = {hinta}/(math.pi * ({pizza} / 2) ** 2)")
    return pizhin


pizza = []
hinta = []
while len(pizza) <= 1:
    pizza.append(float(input("Anna pizzan halkaisija (cm): ")))
    hinta.append(float(input("Anna pizzan hinta (€): ")))
hintapercm = [pizzahinta(pizz, hint) for pizz, hint in zip(pizza, hinta)]
if hintapercm[0] < hintapercm[1]:
    print(f"Ensimmäinen pizza on halvempi. {hintapercm[0]*100:.2f} snt/cm^2")
elif hintapercm[1] < hintapercm[0]:
    print(f"Toinen pizza on halvempi. {hintapercm[1]*100:.2f} snt/cm^2")
else:
    print(f"Molemmat pizzat maksavat saman verran. {hintapercm[0]*100:.2f} snt/cm^2")