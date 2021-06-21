from lesson6.task4.Car import Car


class LimitedCar(Car):

    def __init__(self, limit, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.limit = limit

    def show_speed(self):
        if int(self.speed) > int(self.limit):
            print(f"Speed is too high({self.speed})! Slow down!")
        else:
            Car.show_speed(self)
