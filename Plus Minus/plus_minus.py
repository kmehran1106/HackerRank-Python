import pytest


def plus_minus(array: list) -> list:
    length = len(array)

    positive_count = 0
    negative_count = 0
    neutral_count = 0

    for value in array:
        if value == 0:
            neutral_count += 1
        elif value > 0:
            positive_count += 1
        else:
            negative_count += 1
    return [positive_count/length, negative_count/length, neutral_count/length]


@pytest.fixture
def get_fixtures():
    first_input = [1, 0, -1]
    first_output = [1/3, 1/3, 1/3]

    second_input = [1, 1, 1, 0, 0, -1, -1]
    second_output = [3/7, 2/7, 2/7]
    return [
        (first_input, first_output),
        (second_input, second_output)
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert plus_minus(data[0]) == data[1]
