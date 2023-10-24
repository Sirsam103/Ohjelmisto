import random

class Auto:
    def __init__ (self, input_regis, input_velmax):
        self.regis = input_regis
        self.velmax = input_velmax
        self.velnow = 60
        self.dist = 2000
    def accelerate(self, input_velchange):
        self.velnow += input_velchange
        if (self.velnow > self.velmax):
            self.velnow = self.velmax
        elif (self.velnow < 0):
            self.velnow = 0
    def move (self, input_timeused):
        self.dist += self.velnow * input_timeused

auto = Auto(f"ABC-123", 142)
auto.move(1.5)
print(auto.dist)