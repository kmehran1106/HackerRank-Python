import pytest
from typing import List


def minimum_distances(array: List[int]) -> int:
    r = 10**5
    f = False
    m = dict()
    for i, v in enumerate(array):
        x = m.get(v, [])
        if not x:
            m[v] = [i]
        else:
            m[v].append(i)
    for k, v in m.items():
        if len(v) >= 2:
            f = True
            t = v[1] - v[0]
            if t < r:
                r = t
    return r if f else -1


class CaseObject:
    def __init__(self, array: List[int], output: int):
        self.input = array
        self.output = output


@pytest.fixture
def get_fixtures():
    return [
        CaseObject(array=[7, 1, 3, 4, 1, 7,], output=3),
        CaseObject(array=[1, 2, 3, 4, 10], output=-1),
    ]


def test_code(get_fixtures):
    for test in get_fixtures:
        assert minimum_distances(test.input) == test.output
