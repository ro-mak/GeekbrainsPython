from lesson6.task5.Stationary import Stationary


class Pen(Stationary):
    def draw(self):
        print(f"Drawing with a {self.title} Pen")
