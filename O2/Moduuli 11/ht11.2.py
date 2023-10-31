from auto import Car


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
