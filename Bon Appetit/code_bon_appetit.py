import pytest
from typing import List


def bon_appetit(array: List[int], index: int, paid: int) -> int:
    array.pop(index)
    bill = sum(array) // 2
    
    if paid <= bill:
        return 0
    else:
        return paid - bill


@pytest.fixture
def get_fixtures():
    first_input = [
        [3, 10, 2, 9], 1, 12
    ]
    first_output = 5

    second_input = [
        [3, 10, 2, 9], 1, 7
    ]
    second_output = 0

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert bon_appetit(*data[0]) == data[1]