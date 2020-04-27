import pytest
from typing import List


def migratory_birds(array: List[int]) -> int:
    maximum = array[0]
    count_dict = {
        maximum: 1
    }

    for num in array[1:]:
        if not count_dict.get(num, None):
            count_dict[num] = 1
        else:
            count_dict[num] += 1

        if count_dict[num] > count_dict[maximum]:
            maximum = num
        elif count_dict[num] == count_dict[maximum] and num < maximum:
            maximum = num
        
    return maximum
    
@pytest.fixture
def get_fixtures():
    first_input = [1, 4, 4, 4, 5, 3]
    first_output = 4

    return [
        (first_input, first_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert migratory_birds(data[0]) == data[1]