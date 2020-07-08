import pytest
from typing import List


def repeating_strings(s: str, n: int) -> int:
    full = n // len(s)
    extras = n % len(s)
    # get number of "a" inside the string s
    c1 = len(list(filter(lambda x: x == "a", s)))
    # get number of "a" inside the string s multiplied by the full iterations under n
    cf = c1 * full
    # get number of "a" inside the string s to completely fulfill n if n isn't divisible by len(s)
    ce = len(list(filter(lambda x: x == "a", s[:extras])))
    return cf + ce


@pytest.fixture
def get_fixtures():
    first_input = ["aba", 10]
    first_output = 7

    second_input = ["a", 1000000000000]
    second_output = 1000000000000

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert repeating_strings(*data[0]) == data[1]
