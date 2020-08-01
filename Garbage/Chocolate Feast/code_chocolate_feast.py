import pytest


def chocolate_feast(n: int, c: int, m: int) -> int:
    result = n // c
    wrappers = result
    while wrappers >= m:
        result += wrappers // m
        wrappers = wrappers // m + wrappers % m
    return result


class CaseObject:
    def __init__(self, n: int, c: int, m: int, output: int):
        self.n, self.c, self.m = n, c, m
        self.output = output


@pytest.fixture
def get_fixtures():
    return [
        CaseObject(7, 3, 2, output=3),
        CaseObject(10, 2, 5, output=6),
        CaseObject(12, 4, 4, output=3),
        CaseObject(6, 2, 2, output=5),
    ]


def test_code(get_fixtures):
    for test in get_fixtures:
        assert chocolate_feast(test.n, test.c, test.m) == test.output
