import pytest
from typing import List

def pdf_viewer(heights: List[int], string: str) -> int:
    diff = 97
    max = 0
    for c in string:
        m = heights[ord(c) - diff]
        max = m if m > max else max
    return max * len(string)
    

@pytest.fixture
def get_fixtures():
    first_input = [
        [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7],
        "abc",
    ]
    first_output = 9

    return [
        (first_input, first_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert pdf_viewer(*data[0]) == data[1]