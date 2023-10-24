class Auto:
    def __init__ (self, input_regis, input_velmax):
        self.regis = input_regis
        self.velmax = input_velmax
        self.velnow = 0
        self.dist = 0
    def accelerate(self, input_velchange):
        self.velnow += input_velchange
        if (self.velnow > self.velmax):
            self.velnow = self.velmax
        elif (self.velnow < 0):
            self.velnow = 0


uusi_Auto = Auto('ABC-123', 142)
uusi_Auto.accelerate(30)
uusi_Auto.accelerate(70)
uusi_Auto.accelerate(50)
print(f'{uusi_Auto.velnow}')
uusi_Auto.accelerate(-200)
print(f'{uusi_Auto.velnow}')