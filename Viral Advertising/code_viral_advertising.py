import pytest
from typing import List


def viral_advertising(days: int) -> int:
    l = [0] * days
    l[0] = 2

    i = 1
    while i < days:
        l[i] = int((l[i-1] * 3) / 2)
        i += 1
    return sum(l)


@pytest.fixture
def get_fixtures():
    first_input = 5
    first_output = 24

    second_input = 3
    second_output = 9

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert viral_advertising(data[0]) == data[1]