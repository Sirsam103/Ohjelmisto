le = int(input("Leiviskät: "))
na = int(input("Naulat: "))
lu = int(input("Luodit: "))
mg = ((le*20*32+na*32+lu)*13.3)%1000
mk = (((le*20*32+na*32+lu)*13.3)-mg)/1000
print("Massa yhteensä: ", f"kiloa {mk:.0f} ja ", f"grammaa {mg:.2f}")
