import pytest


"""
 1 2 3 4
 5 6 7 8
 2 4 6 8
 1 3 5 7
"""

def diagonal_difference(array: list) -> int:
    length = len(array) - 1

    first = 0
    second = 0

    for index, sub_array in enumerate(array):
        first += sub_array[index]
        second += sub_array[length - index]
    return abs(first - second)
    

@pytest.fixture
def get_fixtures():
    first_input = [
        [11, 2, 4],
        [4, 5, 6],
        [10, 8, -12]
    ]
    first_output = 15

    second_input = [
        [11, 2, 4, 3],
        [4, 5, 6, 7],
        [10, 8, -12, 1],
        [-2, 4, 5, 3],
    ]
    second_output = 8
    return [
        (first_input, first_output),
        (second_input, second_output)
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert diagonal_difference(data[0]) == data[1]