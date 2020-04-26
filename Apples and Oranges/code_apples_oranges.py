import pytest
from typing import List, Tuple


def apple_and_orange(
        house_start: int, house_end: int, apple_loc: int, orange_loc: int, 
        apples: List[int], oranges: List[int]
    ) -> Tuple[int, int]:
    
    count_apple = 0
    count_orange = 0
    for loc in apples:
        if house_start <= loc + apple_loc <= house_end:
            count_apple += 1
    for loc in oranges:
        if house_start <= loc + orange_loc <= house_end:
            count_orange += 1
    return (count_apple, count_orange)


@pytest.fixture
def get_fixtures():
    first_input = [7, 11, 5, 15, [-2, 2, 1], [5, -6]]
    first_output = (1, 1)

    return [
        (first_input, first_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        input_list = data[0]
        output_val = data[1]
        assert apple_and_orange(*input_list) == output_val