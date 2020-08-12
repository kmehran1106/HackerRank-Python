import pytest
from typing import List
import math


def cavity_map(grid: List[str]) -> List[str]:
    for i in range(1, len(grid) - 1):
        n = grid[i][0]
        for j in range(1, len(grid) - 1):
            top = grid[i-1][j]
            bottom = grid[i+1][j]
            left = grid[i][j-1]
            right = grid[i][j+1]
            x = grid[i][j]
            if x > top and x > bottom and x > left and x > right:
                n += "X"
            else:
                n += x
        n += grid[i][-1]
        grid[i] = n
    return grid


class CaseObject:
    def __init__(self, grid: List[str], output: List[str]):
        self.grid = grid
        self.output = output


@pytest.fixture
def get_fixtures():
    return [
        CaseObject(
            grid=[
                "1112", 
                "1912", 
                "1892", 
                "1234"
            ], 
            output=[
                "1112", 
                "1X12", 
                "18X2", 
                "1234"
            ]
        ),
        CaseObject(grid=["12", "12"], output=["12", "12"]),
    ]


def test_code(get_fixtures):
    for test in get_fixtures:
        assert cavity_map(test.grid) == test.output
