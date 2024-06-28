#
# from math import pi
#
# class Rectangle:
#     def __init__(self, weight, length):
#         self.weight = weight
#         self.length = length
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
# class RightTringle:
#     def __init__(self, side):
#         self.side = side
#
# class Trapezoid:
#     def __init__(self, middleLine, height):
#         self.middleLine = middleLine
#         self.height = height
#
# class Figure(Rectangle, Circle, RightTringle, Trapezoid):
#     def __init__(self, weight, length, radius, side, middleLine, height):
#         self.weight = weight
#         self.length = length
#         self.radius = radius
#         self.side = side
#         self.middleLine = middleLine
#         self.height = height
#
#     def get_s_rect(self):
#         return f'Площадь прямоугольника: {self.weight.weight * self.height.height}'
#
#     def get_s_circ(self):
#         return f'Площадь круга: {pi * self.radius.radius ** 2}'
#
#     def get_s_rightTr(self):
#         return f'Площадь правильного треугольника: {(self.side.side**2 * 3**1/2) / 4}'
#
#     def get_s_trap(self):
#         return f'Площадь трапеции: {self.middleLine.middleLine * self.height.height}'
# rec = Rectangle(12, 6)
# circ = Circle(2)
# rtr = RightTringle(3)
# tr = Trapezoid(3, 5)
# fig = Figure(rec, rec, circ, rtr, tr, tr)
#
# print(fig.get_s_rect())
# print(fig.get_s_circ())
# print(fig.get_s_rightTr())
# print(fig.get_s_trap())


from math import pi

class Figure:
    def __init__(self, name):
        self.name = name

    def get_s(self):
        pass

    def __str__(self):
        return self.name

    def __int__(self):
        pass

class Rectangle(Figure):
    def __init__(self, name, height, weight):
        super().__init__(name)
        self.height = height
        self.weight = weight

    def get_s(self):
        return f'Площадь фигуры {self.name} равна {self.height * self.weight}'

    def __int__(self):
        return self.height * self.weight


class Circle(Figure):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def get_s(self):
        return f'Площадь фигуры {self.name} равна {pi * self.radius ** 2}'

    def __int__(self):
        return pi * self.radius ** 2

class RightTringle(Figure):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def get_s(self):
        return f'Площадь фигуры {self.name} равна {(self.side ** 2 * (3 ** 1 / 2)) / 4}'

    def __int__(self):
        return (self.side ** 2 * (3 ** 1 / 2)) / 4


class Trapezoid(Figure):
    def __init__(self, name, middleLine, height):
        super().__init__(name)
        self.middleLine = middleLine
        self.height = height

    def get_s(self):
        return f'Площадь фигуры {self.name} равна {self.middleLine * self.height}'

    def __int__(self):
        return self.middleLine * self.height


rect = Rectangle('Прямоугольник', 5, 2)
circ = Circle('Окружность', 10)
rtr = RightTringle('Правильный треугольник', 4)
trap = Trapezoid('Трапеция', 5, 3)


print(rect.get_s())
print(circ.get_s())
print(rtr.get_s())
print(trap.get_s())
print()
print(rect.__str__())
print(circ.__str__())
print(rtr.__str__())
print(trap.__str__())
print()
print(rect.__int__())
print(circ.__int__())
print(rtr.__int__())
print(trap.__int__())









