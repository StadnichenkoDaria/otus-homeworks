from oop_homework.src.Figure import Figure
from oop_homework.src.Rectangle import Rectangle


def test_instance(rectangle):
    assert isinstance(rectangle, Rectangle)


def test_inheritance(rectangle):
    assert isinstance(rectangle, Figure)


def test_calculate_area(rectangle):
    assert rectangle.calculate_area(15, 10) == 75


def test_calculate_perimeter(rectangle):
    assert rectangle.calculate_perimeter(3, 4) == 14


def test_add_area(rectangle, triangle):
    rectangle.calculate_area(15, 10)
    triangle.calculate_area(15, 10)
    assert rectangle.add_area(triangle) == 150
