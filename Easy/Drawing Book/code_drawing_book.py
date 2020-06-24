import pytest
import math


def drawing_book(total: int, page: int) -> int:
    if page == 1 or (total % 2 == 0 and page == total) or (total % 2 != 0 and page >= total - 1):
        return 0
    if page <= total // 2:
        turns = (page - 1) / 2
        turns = math.ceil(turns)
    elif total % 2 != 0:
        turns = (total - page) // 2
    else:
        turns = (total - page) / 2
        turns = math.ceil(turns)
    return turns
    

@pytest.fixture
def get_fixtures():
    first_input = [6, 2]
    first_output = 1

    second_input = [5, 4]
    second_output = 0

    third_input = [70809, 46090]
    third_output = 12359

    fourth_input = [6, 5]
    fourth_output = 1
    
    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
        (fourth_input, fourth_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert drawing_book(*data[0]) == data[1]
