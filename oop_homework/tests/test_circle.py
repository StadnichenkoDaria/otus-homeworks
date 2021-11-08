from oop_homework.src.Circle import Circle
from oop_homework.src.Figure import Figure


def test_instance(circle):
    assert isinstance(circle, Circle)


def test_inheritance(circle):
    assert isinstance(circle, Figure)


def test_calculate_area(circle):
    assert circle.calculate_area(10) == 314


def test_calculate_perimeter(circle):
    assert circle.calculate_perimeter(10) == 63


def test_add_area(circle, square):
    circle.calculate_area(10)
    square.calculate_area(15)
    assert circle.add_area(square) == 539
