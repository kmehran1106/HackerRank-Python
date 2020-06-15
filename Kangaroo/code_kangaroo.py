import pytest


def kangaroo(x1: int, v1: int, x2: int, v2: int) -> bool:
    if x1 < x2 and v1 <= v2:
        return False
    else:
        n1 = (x2-x1)/(v1-v2)
        n2 = (x2-x1)//(v1-v2)

        if n1 == n2:
            return True
        else:
            return False


@pytest.fixture
def get_fixtures():
    first_input = [28, 8, 96, 2]
    first_output = False

    second_input = [0, 3, 4, 2]
    second_output = True

    return [
        (first_input, first_output),
        (second_input, second_output)
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert kangaroo(*data[0]) == data[1]