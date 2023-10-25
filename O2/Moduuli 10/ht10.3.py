import random


class Hissi:
    def __init__(self, input_alin, input_ylin):
        self.kerros = input_alin
        self.alin_kerros = input_alin
        self.ylin_kerros = input_ylin

    def up(self):
        self.kerros += 1
        print(f'Kerros: {self.kerros}')

    def down(self):
        self.kerros -= 1
        print(f'Kerros: {self.kerros}')

    def move(self, dest):
        while self.kerros < dest and self.kerros < self.ylin_kerros:
            self.up()
        while self.kerros > dest and self.kerros > self.alin_kerros:
            self.down()
        # print(f'{self.kerros}')


class Talo:
    def __init__(self, input_alin, input_ylin, input_hissit):
        self.hissit = [Hissi(input_alin, input_ylin) for _ in range(input_hissit)]
        self.ylin = input_ylin
        self.alin = input_alin

    def move_lift(self, hissi_nro, input_dest):
        if hissi_nro < 1 or hissi_nro > len(self.hissit):
            print(f'Hissiä {hissi_nro} ei ole.')
            return
        hissi = self.hissit[hissi_nro - 1]
        hissi.move(input_dest)
        if input_dest < self.alin:
            input_dest = self.alin
        elif input_dest > self.ylin:
            input_dest = self.ylin
        print(f'Hissi {hissi_nro} on nyt kerroksessa {input_dest}')

    def alarm(self):
        for hissi in self.hissit:
            hissi.move(self.alin)


talo = Talo(1, 25, 3)
talo.move_lift(66, 5)
talo.move_lift(3, 927)
for i in range(5):
    talo.move_lift(random.randint(1, 3), random.randint(1, 25))
talo.alarm()
