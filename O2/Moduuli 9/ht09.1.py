class Auto:
    def __init__ (self, input_regis, input_velmax):
        self.regis = input_regis
        self.velmax = input_velmax
        self.velnow = 0
        self.dist = 0

uusi_Auto = Auto('ABC-123', 142)
print(f'Auton rekisteritunnus on: {uusi_Auto.regis}\nAuton huippunopeus on: {uusi_Auto.velmax} km/h\nAuton tämänhetkinen nopeus on: {uusi_Auto.velnow} km/h ja autolla on kuljettu {uusi_Auto.dist} kilometriä')
