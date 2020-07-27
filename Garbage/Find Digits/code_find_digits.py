import pytest


def find_digits(x: int) -> int:
    c = 0
    y = x
    while y > 0:
        n = y % 10
        if n != 0 and x % n == 0:
            c += 1
        y = y // 10
    return c


@pytest.fixture
def get_fixtures():
    first_input = 121
    first_output = 2

    second_input = 114108089
    second_output = 3

    third_input = 110110015
    third_output = 6

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert find_digits(data[0]) == data[1]
