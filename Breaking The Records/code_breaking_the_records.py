import pytest
from typing import List

def break_the_record(array: List[int]) -> List[int]:
    minimum = array[0]
    maximum = array[0]

    min_record = 0
    max_record = 0

    for num in array[1:]:
        if minimum <= num <= maximum:
            continue
        elif num < minimum:
            min_record += 1
            minimum = num
        elif num > maximum:
            max_record += 1
            maximum = num
    return [max_record, min_record]


@pytest.fixture
def get_fixtures():
    first_input = [10, 5, 20, 20, 4, 5, 2, 25, 1]
    first_output = [2, 4]

    return [
        (first_input, first_output)
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert break_the_record(data[0]) == data[1]