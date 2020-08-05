import pytest
from typing import List
import math


def get_special_problems_from_workbook(n: int, k: int, arr: List[int]) -> int:
    output = 0
    page = 1
    for chapter in range(n):
        ch_problems = arr[chapter]
        for problem in range(1, ch_problems+1):
            if problem == page:
                output += 1
            if problem % k == 0 or problem == ch_problems:
                page += 1
    return output


class CaseObject:
    def __init__(self, n: int, k: int, arr: List[int], output: int):
        self.n, self.k, self.arr = n, k, arr
        self.output = output


@pytest.fixture
def get_fixtures():
    return [
        CaseObject(5, 3, [4, 2, 6, 1, 10,], output=4),
        CaseObject(10, 5, [3, 8, 15, 11, 14, 1, 9, 2, 24, 31,], output=8),
        CaseObject(
            40, 
            7, 
            [
                1, 10, 12, 4, 11, 6, 8, 15, 23, 24, 23, 24, 39, 34, 50, 3,
                58, 62, 71, 79, 95, 100, 2, 2, 100, 100, 100, 100, 100, 100, 1,
                100, 100, 100, 100, 100, 3, 100, 100, 100,
            ],
            output=12
        )
    ]


def test_code(get_fixtures):
    for test in get_fixtures:
        assert get_special_problems_from_workbook(test.n, test.k, test.arr) == test.output
