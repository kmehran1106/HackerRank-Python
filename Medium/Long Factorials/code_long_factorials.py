import pytest


def long_factorials(n: int) -> int:
    x = 1
    for i in range(2, n+1):
        x *= i
    return x


@pytest.fixture
def get_fixtures():
    first_input = 25
    first_output = 15511210043330985984000000

    second_input = 45
    second_output = 119622220865480194561963161495657715064383733760000000000

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert long_factorials(data[0]) == data[1]
