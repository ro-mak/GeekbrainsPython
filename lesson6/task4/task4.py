import random

from lesson6.task4.PoliceCar import PoliceCar
from lesson6.task4.SportCar import SportCar
from lesson6.task4.TownCar import TownCar
from lesson6.task4.WorkCar import WorkCar

cars = [
    SportCar(color="Red", name="Ferrari", speed="320"),
    WorkCar(color="Black", name="Kamaz", speed="41"),
    PoliceCar(color="White", name="Ford", speed="100"),
    TownCar(color="Green", name="Volkswagen", speed="69"),
    TownCar(color="Blue", name="Nissan", speed="39")
]

directions = [
    "STRAIGHT",
    "BACK",
    "RIGHT",
    "LEFT"
]

i = 0
while i < 10:
    car = cars[random.randint(0, len(cars)-1)]
    print(f"Car info: {vars(car)}")
    car.go()
    car.show_speed()
    car.turn(directions[random.randint(0, len(directions)-1)])

    i += 1
