import math

from oop_homework.src.Figure import Figure


class Circle(Figure):

    # вычислить площать круга (S = Пr^2)
    def calculate_area(self, circle_radius):
        self.area = round(math.pi * circle_radius ** 2)
        return self.area

    # вычислить периметр круга (P = 2Пr)
    def calculate_perimeter(self, circle_radius):
        self.perimeter = round(2 * math.pi * circle_radius)
        return self.perimeter
