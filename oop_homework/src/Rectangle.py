from oop_homework.src.Figure import Figure


class Rectangle(Figure):

    # вычислить площать прямоугольника (S = a * b)
    def calculate_area(self, side_a, side_b):
        self.area = 0.5 * side_a * side_b
        return self.area

    # вычислить периметр прямоугольника (P = (a + b) * 2)
    def calculate_perimeter(self, side_a, side_b):
        self.perimeter = (side_a + side_b) * 2
        return self.perimeter
