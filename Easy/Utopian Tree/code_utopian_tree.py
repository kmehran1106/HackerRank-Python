import pytest


def utopian_tree(cycles: int) -> int:
    h = 1
    for i in range(1, cycles+1):
        h = h * 2 if i % 2 == 1 else h + 1
    return h
    

@pytest.fixture
def get_fixtures():
    first_input = 4
    first_output = 7

    second_input = 5
    second_output = 14

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert utopian_tree(data[0]) == data[1]