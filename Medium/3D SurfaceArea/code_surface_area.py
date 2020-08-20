import pytest
from typing import List
import math


def surface_area(grid: List[List[int]]) -> int:
    # area initialised with bottom and top area, 2 * height * width
    area = 2 * len(grid) * len(grid[0])

    a = list()

    # append 0 before and after the first and last elements of each row respectively
    for row in grid:
        a.append([0] + row + [0])
    
    x = [
        [0] * (len(grid[0]) + 2) 
    ]

    # append a row of 0's to the top and bottom of the 2d grid
    a = x + a + x
    print(a)
    
    # the area of sides is the sum of difference of adjacent cells
    for i in range(1, len(a)):
        for j in range(1, len(a[i])):
            area += abs(a[i][j] - a[i-1][j])
            area += abs(a[i][j] - a[i][j-1])
    return area


class CaseObject:
    def __init__(self, grid: List[List[int]], output: int):
        self.grid = grid
        self.output = output


@pytest.fixture
def get_fixtures():
    return [
        CaseObject(
            grid=[
                [1]
            ],
            output=6
        ),
        CaseObject(
            grid=[
                [1, 3, 4],
                [2, 2, 3],
                [1, 2, 4],
            ],
            output=60
        ),
    ]


def test_code(get_fixtures):
    for test in get_fixtures:
        assert surface_area(test.grid) == test.output
