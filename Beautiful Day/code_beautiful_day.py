import pytest


def beautiful_days(start: int, end:int, divisor: int) -> int:
    array = [i for i in range(start, end+1)]
    array = list(filter(lambda x: abs(int(str(x)) - int(str(x)[::-1]))%divisor == 0, array))
    return len(array)


@pytest.fixture
def get_fixtures():
    first_input = [20, 23, 6]
    first_output = 2

    return [
        (first_input, first_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert beautiful_days(*data[0]) == data[1]