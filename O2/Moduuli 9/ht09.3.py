import random

class Auto:
    def __init__ (self, input_regis, input_velmax):
        self.regis = input_regis
        self.velmax = input_velmax
        self.velnow = 60
        self.dist = 0
    def accelerate(self, input_velchange):
        self.velnow += input_velchange
        if (self.velnow > self.velmax):
            self.velnow = self.velmax
        elif (self.velnow < 0):
            self.velnow = 0
    def move (self, input_timeused):
        self.dist += self.velnow * input_timeused


auto_lista = []
for i in range(1, 11):
    auto = Auto(f"ABC-{i}", random.randint(100, 200))
    auto_lista.append(auto)

runs = 0
while True:
    for auto in auto_lista:
        auto.accelerate(random.randint(-10, 15))
        auto.move(1)
        #print(f'{auto.regis}, {auto.velnow}, {auto.dist}, {runs}')
        if auto.dist >= 10000:
            print(f'''Auto {auto.regis} voitti kilpailun!!!
Kilpailussa kesti {runs} tuntia\n
Autojen ominaisuudet ovat:
Rekisteritunnus, kuljettu matka, huippunopeus, tämänhetkinen nopeus.''')
            for auto in auto_lista:
                print(f'{auto.regis, auto.dist, auto.velmax, auto.velnow}')
            exit(0)
    runs += 1