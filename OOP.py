import math
print(math.sqrt(3.14))
import my
my.greeting()


class Car:
    def __init__(self, color):
        self.color = color

    def start(self):
        print(f"{self.color} car started")

my_car = Car("Red")
my_car.start()


