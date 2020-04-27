import pytest
from typing import List


def divisible_sum_pairs(array: List[int], divisor: int) -> int:
    count = 0

    for index, num in enumerate(array):
        m = list(
            filter(lambda x: (x + num) % divisor == 0, array[index+1:])
        )
        count += len(m)
    return count

    
@pytest.fixture
def get_fixtures():
    first_input = [
        [1, 3, 2, 6, 1, 2], 3
    ]
    first_output = 5

    return [
        (first_input, first_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert divisible_sum_pairs(*data[0]) == data[1]