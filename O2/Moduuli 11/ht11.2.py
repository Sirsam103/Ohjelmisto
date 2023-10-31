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


class Gas(Car):
    def __init__(self, input_regis, input_velmax, input_velnow, input_tank):
        super().__init__(input_regis, input_velmax, input_velnow)
        self.tank = input_tank


class Electric(Car):
    def __init__(self, input_regis, input_velmax, input_velnow, input_battery):
        super().__init__(input_regis, input_velmax, input_velnow)
        self.battery = input_battery


gas_car = Gas("ACD-123", 165, 123, 32.3, )
ev = Electric("ABC-15", 180, 123, 52.5)
gas_car.move(3)
ev.move(3)
print(f"{'Polttomoottori auto kulki: ':<30}{gas_car.dist}km\n{'Sähköauto kulki: ':<30}{ev.dist}km")
