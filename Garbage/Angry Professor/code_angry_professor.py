import pytest
from typing import List

def is_cancelled(threshold: int, array: List[int]) -> bool:
    array = list(filter(lambda x: x <=0, array))
    return len(array) < threshold


@pytest.fixture
def get_fixtures():
    first_input = [3, [-1, -3, 4, 2]]
    first_output = True

    second_input = [2, [0, -1, 2, 1]]
    second_output = False

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert is_cancelled(*data[0]) == data[1]