class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} is moving")

    def stop(self):
        print(f"{self.name} is stopping")

    def turn(self, direction):
        print(f"{self.name} is turning {direction}")

    def show_speed(self):
        print(f"Current speed: {self.speed}")
