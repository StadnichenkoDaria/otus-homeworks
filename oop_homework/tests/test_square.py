from oop_homework.src.Figure import Figure
from oop_homework.src.Square import Square


def test_instance(square):
    assert isinstance(square, Square)


def test_inheritance(square):
    assert isinstance(square, Figure)


def test_calculate_area(square):
    assert square.calculate_area(15) == 225


def test_calculate_perimeter(square):
    assert square.calculate_perimeter(3) == 12


def test_add_area(square, rectangle):
    square.calculate_area(15)
    rectangle.calculate_area(15, 10)
    assert square.add_area(rectangle) == 300
