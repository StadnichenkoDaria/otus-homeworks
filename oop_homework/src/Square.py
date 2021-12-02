from oop_homework.src.Figure import Figure


class Square(Figure):

    # вычислить площать квадрата (S = a^2)
    def calculate_area(self, side_a):
        self.area = side_a ** 2
        return self.area

    # вычислить периметр квадрата (P = 4 * a)
    def calculate_perimeter(self, side_a):
        self.perimeter = side_a * 4
        return self.perimeter
