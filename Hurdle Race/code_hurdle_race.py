import pytest
from typing import List


def hurdle_race(jump: int, hurdles: List[int]) -> int:
    m = max(hurdles)
    return m - jump if m > jump else 0


@pytest.fixture
def get_fixtures():
    first_input = [4, [1, 6, 3, 5, 2]]
    first_output = 2

    second_input = [8, [1, 6, 3, 5, 2]]
    second_output = 0

    return [
        (first_input, first_output),
        (second_input, second_output)
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert hurdle_race(*data[0]) == data[1]