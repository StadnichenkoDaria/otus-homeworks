from oop_homework.src.Figure import Figure
from oop_homework.src.Triangle import Triangle


def test_instance(triangle):
    assert isinstance(triangle, Triangle)


def test_inheritance(triangle):
    assert isinstance(triangle, Figure)


def test_calculate_area(triangle):
    assert triangle.calculate_area(15, 10) == 75.0


def test_calculate_perimeter(triangle):
    assert triangle.calculate_perimeter(3, 4, 2) == 9


def test_add_area(triangle, circle):
    triangle.calculate_area(15, 10)
    circle.calculate_area(10)
    assert triangle.add_area(circle) == 389
