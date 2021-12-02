import pytest as pytest

from oop_homework.src.Circle import Circle
from oop_homework.src.Rectangle import Rectangle
from oop_homework.src.Square import Square
from oop_homework.src.Triangle import Triangle


@pytest.fixture()
def triangle():
    return Triangle("triangle", side_a=5, side_b=3, side_c=4)


@pytest.fixture()
def circle():
    return Circle("circle")


@pytest.fixture()
def rectangle():
    return Rectangle("rectangle")


@pytest.fixture()
def square():
    return Square("square")
