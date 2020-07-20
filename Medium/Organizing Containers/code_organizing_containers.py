import pytest
from typing import List


def organzing_containers(containers: List[List[int]]) -> bool:
    row_totals = sorted([ sum(x) for x in containers])
    col_totals = sorted([ sum(x) for x in zip(*containers)])
    return row_totals == col_totals


@pytest.fixture
def get_fixtures():
    first_input = [
        [1, 1],
        [1, 1]
    ]
    first_output = True

    second_input = [
        [0, 2],
        [1, 1]
    ]
    second_output = False

    third_input = [
        [1, 3, 1],
        [2, 1, 2],
        [3, 3, 3]
    ]
    third_output = False

    fourth_input = [
        [0, 2, 1],
        [1, 1, 1],
        [2, 0, 0]
    ]
    fourth_output = True


    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
        (fourth_input, fourth_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert organzing_containers(data[0]) == data[1]
