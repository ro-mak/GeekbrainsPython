from lesson6.task4.LimitedCar import LimitedCar


class TownCar(LimitedCar):
    def __init__(self, speed, color, name):
        super().__init__(60, speed, color, name, is_police=False)
