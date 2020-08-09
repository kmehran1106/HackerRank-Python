import pytest
from typing import List, Optional
import math


def fair_rations(array: List[int]) -> Optional[int]:
    count = 0
    if sum(array) % 2 != 0:
        return None

    for i in range(0, len(array) - 1):
        if array[i] % 2 != 0:
            array[i] = array[i] + 1
            array[i+1] = array[i+1] + 1
            count += 2
    return count


class CaseObject:
    def __init__(self, array: List[int], output: Optional[int]):
        self.array = array
        self.output = output


@pytest.fixture
def get_fixtures():
    return [
        CaseObject(array=[2, 3, 4, 5, 6,], output=4),
        CaseObject(array=[1, 2], output=None),
    ]


def test_code(get_fixtures):
    for test in get_fixtures:
        assert fair_rations(test.array) == test.output
