import pytest
from typing import List


def equalize_array(array: List[int]) -> int:
    f = 0
    m = 0
    for v in array:
        frequency = array.count(v)
        if frequency > f:
            f = frequency
            m = v
    return len(array) - f


@pytest.fixture
def get_fixtures():
    first_input = [3, 3, 2, 1, 3,]
    first_output = 2

    second_input = [1, 2, 3, 1, 2, 3, 3, 3,]
    second_output = 4

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert equalize_array(data[0]) == data[1]
