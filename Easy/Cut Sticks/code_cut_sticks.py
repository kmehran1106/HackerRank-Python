import pytest
from typing import List


def cut_sticks(input: List[int]) -> List[int]:
    r = list()
    l = len(input)
    p = -1
    input.sort()
    for i, v in enumerate(input):
        if v > p:
            r.append(l)
        l -= 1
        p = v
    return r


@pytest.fixture
def get_fixtures():
    first_input = [5, 4, 4, 2, 2, 8]
    first_output = [6, 4, 2, 1]

    second_input = [1, 2, 3, 4, 3, 3, 2, 1]
    second_output = [8, 6, 4, 1]

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert cut_sticks(data[0]) == data[1]
