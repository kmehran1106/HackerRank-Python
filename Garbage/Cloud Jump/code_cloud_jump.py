import pytest
from typing import List


def cloud_jump(clouds: List[int]) -> int:
    i = 0
    k = 0
    last = len(clouds) - 1
    while i < last - 2:
        if clouds[i+2] == 0:
            i += 2
        else:
            i += 1
        k += 1
    return k + 1


@pytest.fixture
def get_fixtures():
    first_input = [0, 0, 1, 0, 0, 1, 0,]
    first_output = 4

    second_input = [0, 0, 0, 1, 0, 0,]
    second_output = 3

    return [
        (first_input, first_output),
        (second_input, second_output)
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert cloud_jump(data[0]) == data[1]