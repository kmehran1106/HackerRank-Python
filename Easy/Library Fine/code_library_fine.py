import pytest
import math
from typing import List

FINE_Y = 10000
FINE_M = 500
FINE_D = 15

def library_fine(d1: int, m1: int, y1: int, d2: int, m2: int, y2: int) -> int:
    if y1 > y2:
        return FINE_Y
    elif y1 < y2:
        return 0
    else:
        if m1 > m2:
            return FINE_M * (m1 - m2)
        elif m1 < m2:
            return 0
        else:
            return FINE_D * (d1 - d2) if d1 > d2 else 0


@pytest.fixture
def get_fixtures():
    first_input = [9, 6, 2015, 6, 6, 2015,]
    first_output = 45

    second_input = [2, 7, 1014, 1, 1, 1014,]
    second_output = 3000

    third_input = [2, 6, 2014, 7, 6, 2014,]
    third_output = 0

    fourth_input = [15, 7, 2014, 1, 7, 2015]
    fourth_output = 0

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
        (fourth_input, fourth_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert library_fine(*data[0]) == data[1]
