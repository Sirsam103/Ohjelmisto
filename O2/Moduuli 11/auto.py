class Car:
    def __init__(self, input_regis, input_velmax, input_velnow):
        self.regis = input_regis
        self.velmax = input_velmax
        self.velnow = input_velnow
        self.dist = 0

    def accelerate(self, input_velchange):
        self.velnow += input_velchange
        if self.velnow > self.velmax:
            self.velnow = self.velmax
        elif self.velnow < 0:
            self.velnow = 0

    def move(self, input_timeused):
        self.dist += self.velnow * input_timeused