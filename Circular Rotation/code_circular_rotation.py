import pytest
from typing import List

def circular_rotation(array: List[int], rotations: int) -> List[int]:
    rotations = rotations % len(array)
    array = array[-rotations:] + array[:-rotations]
    return array     


@pytest.fixture
def get_fixtures():
    first_input = [
        [1, 2, 3], 2
    ]
    first_output = [2, 3, 1]

    return [
        (first_input, first_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert circular_rotation(*data[0]) == data[1]