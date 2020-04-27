import pytest
from typing import List

def birthday_bar(array: List[int], date: int, month: int) -> int:
    result = 0

    temp = array[:-month+1]

    for index, num in enumerate(temp):
        i = 1
        s = num
        while i < month:
            s = s + array[index+i]
            i += 1
        if s == date:
            result += 1
    return result            


@pytest.fixture
def get_fixtures():
    first_input = [
        [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1], 18, 7
    ]
    first_output = 3

    second_input = [
        [1, 2, 1, 3, 2], 3, 2
    ]
    second_output = 2
    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert birthday_bar(*data[0]) == data[1]