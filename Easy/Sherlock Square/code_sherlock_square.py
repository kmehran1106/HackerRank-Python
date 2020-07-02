import pytest
import math
from typing import List


def sherlock_square(a: int, b: int) -> int:
    """
    [
        Find the Number of Square Integers in between a and b 
        (i.e. numbers whose square root is also a valid integer)

        Here, I've taken the sq. root of a and b
        And counted the number of integers between sqrt(a) and sqrt(b)
    ]

    Args:
        a (int): [Lower Range]
        b (int): [Upper Range]

    Returns:
        int: [Count of Integers in between a and b whose square root is also a valid integer]
    """
    x = math.ceil(math.sqrt(a))
    y = math.floor(math.sqrt(b))
    return y - x + 1


@pytest.fixture
def get_fixtures():
    first_input = [3, 9]
    first_output = 2

    second_input = [17, 24]
    second_output = 0

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert sherlock_square(*data[0]) == data[1]
