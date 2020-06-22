import pytest
from typing import List


def save_the_prisoner(prisoner_count: int, sweet_count: int, start_chair: int):
    """
    [
        if sweets > prisoners, then we need to find the remainder sweets after full passes
        then, we'll be able to find out the last prisoner
        the edge case here however is if sweets > prisoners and sweets is a multiple of prisoners
        then, this means in the final pass, the number of sweets remaining will be equal to prisoners

        start = 6
        prisoners -> 1 2 3 4 5 6 7

        here, we subtracted one from start_chair, because the start_chair itself needs to receive
        the candy.

    ]   

    Args:
        prisoner_count (int): [description]
        sweet_count (int): [description]
        start_chair (int): [description]

    Returns:
        [type]: [description]
    """
    sweet_count = sweet_count % prisoner_count if sweet_count > prisoner_count else sweet_count
    if sweet_count == 0:
        sweet_count = prisoner_count
    start_chair -= 1
    diff = prisoner_count - start_chair
    if diff >= sweet_count:
        return start_chair + sweet_count 
    else:
        return sweet_count - diff


@pytest.fixture
def get_fixtures():
    first_input = [5, 2, 1]
    first_output = 2

    second_input = [5, 2, 2]
    second_output = 3

    third_input = [7, 19, 2]
    third_output = 6

    fourth_input = [13, 140874526, 1]
    fourth_output = 13

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
        (fourth_input, fourth_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert save_the_prisoner(*data[0]) == data[1]