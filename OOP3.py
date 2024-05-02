from OOP2 import Point
import math


class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return f'Circle (x={self.x}, y={self.y}, radius={self.radius})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        radius = self.radius + other.radius
        return f'сложение метод: add {Circle(x, y, radius)}'

    def __sub__(self, other):
        if self.radius == other.radius:
            return Point(self.x, self.y)

        x_sub = (self.x + other.x) / 2
        y_sub = (self.x + other.y) / 2

        radius_sub = abs(self.radius - other.radius)

        return Circle(x_sub, y_sub, radius_sub)


    def area(self):
        return math.pi * (self.radius ** 2)


x_1 = Circle(2, 5, 2)
x_2 = Circle(2, 5, 2)
print(x_1)
print(x_1.distance_from_origin())
print(x_1.area())

print(x_1 + x_2)
print(x_1 - x_2)

