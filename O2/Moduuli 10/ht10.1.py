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


h = Hissi(1, 25)
h.move(260)
h.move(-10)
