import random


class Auto:
    def __init__(self, input_regis, input_velmax):
        self.regis = input_regis
        self.velmax = input_velmax
        self.velnow = 60
        self.dist = 0

    def accelerate(self, input_velchange):
        self.velnow += input_velchange
        if self.velnow > self.velmax:
            self.velnow = self.velmax
        elif self.velnow < 0:
            self.velnow = 0

    def move(self, input_timeused):
        self.dist += self.velnow * input_timeused


class Kilpailu:
    def __init__(self, input_name, input_lenkm, input_carlist):
        self.name = input_name
        self.len_km = input_lenkm
        self.car_list = input_carlist

    def tunti_kuluu(self):
        for car in self.car_list:
            car.accelerate(random.randint(-10, 15))
            car.move(1)

    def tulosta_tilanne(self):
        print(f"║{'Rekisteri':<15} {'Ajettu':<15} {'Huippunopeus':<15} {'Nykyinen nopeus':<15}║")
        for car in self.car_list:
            print(f"║{car.regis:<15} {car.dist:<15} {car.velmax:<15} {car.velnow:<15}║")

    def kilpailu_ohi(self):
        for car in self.car_list:
            if car.dist >= self.len_km:
                return True
        return False


auto_lista = []
for i in range(1, 11):
    auto_lista.append(Auto(f"ABC-{i}", random.randint(100, 200)))
race = Kilpailu("Suuri romuralli", 8000, auto_lista)
runs = 0
while not race.kilpailu_ohi():
    race.tunti_kuluu()
    if runs % 10 == 0:
        print(f"\n╔════════════╣ Kilpailun tilanne {runs} tunnin jälkeen ╠════════════╗")
        race.tulosta_tilanne()
        print(f"╚═══════════════════════════════════════════════════════════════╝")
    runs += 1
print(f"\n╔════════════╣ Kilpailu päättyi {runs} tunnin jälkeen! ╠════════════╗")
race.tulosta_tilanne()
print(f"╚═══════════════════════════════════════════════════════════════╝")
# ║ ╔ ╗ ═ ╚ ╝ ╠ ╣
