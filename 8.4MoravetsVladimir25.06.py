
from math import pi

class Rectangle:
    def __init__(self, weight, length):
        self.weight = weight
        self.length = length


class Circle:
    def __init__(self, radius):
        self.radius = radius

class RightTringle:
    def __init__(self, side):
        self.side = side

class Trapezoid:
    def __init__(self, middleLine, height):
        self.middleLine = middleLine
        self.height = height

class Figure(Rectangle, Circle, RightTringle, Trapezoid):
    def __init__(self, weight, length, radius, side, middleLine, height):
        self.weight = weight
        self.length = length
        self.radius = radius
        self.side = side
        self.middleLine = middleLine
        self.height = height

    def get_s_rect(self):
        return f'Площадь прямоугольника: {self.weight.weight * self.height.height}'

    def get_s_circ(self):
        return f'Площадь круга: {pi * self.radius.radius ** 2}'

    def get_s_rightTr(self):
        return f'Площадь правильного треугольника: {(self.side.side**2 * 3**1/2) / 4}'

    def get_s_trap(self):
        return f'Площадь трапеции: {self.middleLine.middleLine * self.height.height}'
rec = Rectangle(12, 6)
circ = Circle(2)
rtr = RightTringle(3)
tr = Trapezoid(3, 5)
fig = Figure(rec, rec, circ, rtr, tr, tr)

print(fig.get_s_rect())
print(fig.get_s_circ())
print(fig.get_s_rightTr())
print(fig.get_s_trap())