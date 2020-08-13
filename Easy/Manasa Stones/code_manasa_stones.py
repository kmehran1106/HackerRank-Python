import pytest
from typing import List
import math


def manasa_stones(n: int, a: int, b: int) -> List[int]:
    s = set()
    for i in range(n):
        x = a * (n - 1 -i) + b * i
        s.add(x)
    s = list(s)
    s.sort()
    return s
    

class CaseObject:
    def __init__(self, n: int, a: int, b: int, output: List[str]):
        self.n, self.a, self.b = n, a, b
        self.output = output


@pytest.fixture
def get_fixtures():
    return [
        CaseObject(3, 1, 2, output=[2, 3, 4]),
        CaseObject(4, 10, 100, output=[30, 120, 210, 300]),
    ]


def test_code(get_fixtures):
    for test in get_fixtures:
        assert manasa_stones(test.n, test.a, test.b) == test.output
