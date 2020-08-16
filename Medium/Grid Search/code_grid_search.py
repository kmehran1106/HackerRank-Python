import pytest
from typing import List
import math


def grid_search(grid: List[str], pattern: List[str]) -> bool:
    g_row = len(grid) -1
    g_col = len(grid[0]) -1
    p_row = len(pattern) - 1
    p_col = len(pattern[0]) - 1
    c = 0
    for i in range(g_row - p_row + 1):
        for j in range(g_col - p_col + 1):
            if grid[i][j:j+p_col+1] == pattern[0]:
                for k in range(1, len(pattern)):
                    if grid[i+k][j:j+p_col+1] == pattern[k]:
                        c += 1
                        if c == len(pattern) - 1:
                            return True
                    else:
                        c = 0
    return False
    

class CaseObject:
    def __init__(self, grid: List[str], pattern: List[str], output: bool):
        self.grid, self.pattern = grid, pattern
        self.output = output


@pytest.fixture
def get_fixtures():
    return [
        CaseObject(
            grid=[
                "7283455864",
                "6731158619",
                "8988242643",
                "3830589324",
                "2229505813",
                "5633845374",
                "6473530293",
                "7053106601",
                "0834282956",
                "4607924137",
            ],
            pattern=[
                "9505",
                "3845",
                "3530",
            ],
            output=True),
    ]


def test_code(get_fixtures):
    for test in get_fixtures:
        assert grid_search(test.grid, test.pattern) == test.output
