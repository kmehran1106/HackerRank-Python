import pytest

from typing import Tuple


def min_max_sum(array: list) -> Tuple[int, int]:
    array.sort()

    return (
        sum(array[:-1]),
        sum(array[1:])
    )
    

@pytest.fixture
def get_fixtures():
    first_input = [1, 2, 3, 4, 5]
    first_output = (10, 14)

    return [
        (first_input, first_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert min_max_sum(data[0]) == data[1]
