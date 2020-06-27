import pytest
from typing import List


def jumping_cloud(clouds: List[int], k: int) -> int:
    e = 100
    n = len(clouds)
    # initial case
    i = k % n
    e = e - 3 if clouds[i] == 1 else e - 1
    while i != 0:
        i = (i + k) % n
        e = e - 3 if clouds[i] == 1 else e - 1
    return e


@pytest.fixture
def get_fixtures():
    first_input = [
        [0, 0, 1, 0, 0, 1, 1, 0,], 2
    ]
    first_output = 92

    second_input = [
        [1, 1, 1, 0, 1, 1, 0, 0, 0, 0,], 3
    ]
    second_output = 80

    return [
        (first_input, first_output),
        (second_input, second_output)
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert jumping_cloud(*data[0]) == data[1]