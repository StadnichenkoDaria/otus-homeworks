from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, name):
        self.name = name,
        self.area = 0
        self.perimeter = 0

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    def add_area(self, figure):
        if isinstance(figure, Figure):
            amount_area = figure.area + self.area
            return amount_area
        raise ValueError("It's not figure")
