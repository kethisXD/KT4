import pytest
from main import *
@pytest.mark.parametrize("even", [x for x in range(2, 6000, 2)])
def test_even(even):
    assert is_even(even)
@pytest.mark.parametrize("NotEven", [x for x in range(1, 6000, 2)])
def test_NotEven(NotEven):
    assert False == is_even(NotEven)

@pytest.mark.parametrize("width", [x for x in range(1, 100)])
@pytest.mark.parametrize("length", [x for x in range(1, 100)])
def test_Area(width, length):
    assert calculate_area(width, length) == width * length

triangle_list = [
        # Равносторонние треугольники
        (3, 3, 3, "Равносторонний"),
        (5, 5, 5, "Равносторонний"),

        # Равнобедренные треугольники
        (5, 5, 3, "Равнобедренный"),
        (5, 3, 5, "Равнобедренный"),
        (3, 5, 5, "Равнобедренный"),

        # Разносторонние треугольники
        (3, 4, 5, "Разносторонний"),
        (5, 6, 7, "Разносторонний"),
        (7, 5, 6, "Разносторонний"),

        # Невозможные треугольники
        (1, 2, 3, "Не треугольник"),
        (0, 0, 0, "Не треугольник"),
        (-1, 2, 2, "Не треугольник"),
    ]
@pytest.mark.parametrize("a, b, c, expected", triangle_list)
def test_classify_triangle(a, b, c, expected):
    assert classify_triangle(a,b,c) == expected