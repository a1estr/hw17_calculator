import pytest
from app.app import add, subtract, multiply, divide


@pytest.mark.parametrize(
    "value1, value2, expected_result",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (1, -2, -1),
        (0, 0, 0)
    ]
)
def test_add(value1, value2, expected_result):
    """Тестирует функцию сложения."""
    assert add(value1, value2) == expected_result


@pytest.mark.parametrize(
    "value1, value2, expected_result",
    [
        (10, 2, 5),
        (9, 3, 3),
        (5, 2, 2.5)
    ]
)
def test_divide(value1, value2, expected_result):
    """Тестирует функцию деления."""
    assert divide(value1, value2) == expected_result


@pytest.mark.parametrize(
    "value1, value2",
    [
        (5, 0),
        (100, 0),
        (100.5, 0)
    ]
)
def test_divide_invalid(value1, value2):
    """Тестирует выброс исключения при делении"""
    with pytest.raises(ValueError):
        divide(value1, value2)


@pytest.mark.parametrize(
    "value1, value2, expected_result",
    [
        (5, 8, 40),
        (8, 5, 40),
        (0, 3, 0),
        (-5, 8, -40),
        (5, -8, -40),
        (-5, -8, 40),
    ]
)
def test_multiply(value1, value2, expected_result):
    """
    Тестирует функцию умножения
    """
    assert multiply(value1, value2) == expected_result


@pytest.mark.parametrize(
    "value1, value2, expected_result",
    [
        (10, 7, 3),
        (5, 11, -6),
        (-10, 11, -21),
        (10, -11, 21),
        (-10, -11, 1)
    ]
)
def test_subtract(value1, value2, expected_result):
    """
    Тестирует функцию вычитания
    """
    assert subtract(value1, value2) == expected_result
