import pytest


def halloween_sale(p: int, d: int, m: int, s: int) -> int:
    if s < p:
        return 0
    s = s - p
    c = 1
    while s > 0:
        p = p - d if p - d > m else m
        if s - p < 0:
            break
        s -= p
        c += 1
    return c


class CaseObject:
    def __init__(self, p: int, d: int, m: int, s: int, output: int):
        self.p, self.d, self.m, self.s = p, d, m, s
        self.output = output


@pytest.fixture
def get_fixtures():
    return [
        CaseObject(20, 3, 6, 80, output=6),
        CaseObject(20, 3, 6, 85, output=7),
    ]


def test_code(get_fixtures):
    for test in get_fixtures:
        assert halloween_sale(test.p, test.d, test.m, test.s) == test.output
