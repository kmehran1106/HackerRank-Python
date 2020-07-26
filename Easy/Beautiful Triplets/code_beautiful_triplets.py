import pytest
from typing import List


def beautiful_triplets(d: int, array: List[int]) -> int:
    c = 0
    m = dict()
    for i in array: 
        m[i] = True
    for i in array:
        c = c + 1 if m.get(i+d, False) and m.get(i+2*d, False) else c
    return c


@pytest.fixture
def get_fixtures():
    first_input = [3, [1, 2, 4, 5, 7, 8, 10,]]
    first_output = 3

    second_input = [3, [1, 6, 7, 7, 8, 10, 12, 13, 14, 19,]]
    second_output = 2

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert beautiful_triplets(*data[0]) == data[1]