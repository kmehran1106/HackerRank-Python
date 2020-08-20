import pytest
from typing import List
import math


def surface_area(n: int, k: int) -> List[int]:
    a = dict()
    for i in range(1, n+1):
        a[i] = True
        
    t = [i for i in range(1, n+1)]
    l = list()

    if k == 0:
        l = t
    elif (n/k) % 2 != 0: 
        l = [-1]
    else:
        case = True
        for i in range(1, n+1):
            if case:
                l.append(i+k)
            else:
                l.append(i-k)
            if i % k == 0:
                case = not case

    return l


class CaseObject:
    def __init__(self, n: int, k: int, output: List[int]):
        self.n, self.k = n, k
        self.output = output


@pytest.fixture
def get_fixtures():
    return [
        CaseObject(
            n=2, k=1,
            output=[2, 1]
        ),
        CaseObject(
            n=3, k=0,
            output=[1, 2, 3]
        ),
        CaseObject(
            n=3, k=2,
            output=[-1]
        ),
        CaseObject(
            n=10, k=1,
            output=[2, 1, 4, 3, 6, 5, 8, 7, 10, 9]
        ),
    ]


def test_code(get_fixtures):
    for test in get_fixtures:
        assert surface_area(test.n, test.k) == test.output
