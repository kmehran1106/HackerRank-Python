import pytest

START_TIME = 1
START_VALUE = 3

def strange_counter(t: int) -> int:
    x, y = START_TIME, START_VALUE
    while t > y:
        x += y
        y *= 2
        if t < 2*y:
            break
    m = t - x
    return y - m
    

class CaseObject:
    def __init__(self, t: int, output: int):
        self.t = t
        self.output = output


@pytest.fixture
def get_fixtures():
    return [
        CaseObject(4, output=6),
        CaseObject(17, output=5),
    ]


def test_code(get_fixtures):
    for test in get_fixtures:
        assert strange_counter(test.t) == test.output