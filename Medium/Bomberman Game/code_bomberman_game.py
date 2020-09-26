import pytest
from typing import List
import math


def bombaerman_game(seconds: int, grid: List[str]) -> List[str]:
    if seconds < 2:
        return grid
    elif seconds % 2 == 0:
        row = "O" * len(grid[0])
        grid  = [row for i in range(0, len(grid))]
        return grid
    else:
        grid = [x.replace('O', '2') for x in grid]
        grid = [x.replace('.', '0') for x in grid]
        grid = [list(map(int, list(x))) for x in grid]
        
        R = len(grid)
        C = len(grid[0])
        t = 1
        
        while t < 4 + seconds % 4:
            t += 1
            destroyed = set()
            for r in range(R):
                for c in range(C):
                    if grid[r][c] > 0: 
                        grid[r][c] -= 1
                    
                    if t % 2 == 0 and grid[r][c] == 0: 
                        grid[r][c] = 3
                    elif grid[r][c] == 0:
                        destroyed.add((r, c))
                        if r < R-1: 
                            destroyed.add((r+1, c))
                        if r > 0: 
                            destroyed.add((r-1, c))
                        if c < C-1: 
                            destroyed.add((r, c+1))
                        if c > 0: 
                            destroyed.add((r, c-1))
            if destroyed:
                grid = [[2] * len(x) for x in grid]
                for r, c in destroyed:
                    grid[r][c] = 0
        
        grid = [''.join(list(map(str, x))) for x in grid]
        grid = [x.replace('2', 'O') for x in grid]
        grid = [x.replace('0', '.') for x in grid]
        return grid


class CaseObject:
    def __init__(self, seconds: int, grid: List[str], output: List[str]):
        self.seconds, self.grid = seconds, grid
        self.output = output


@pytest.fixture
def get_fixtures():
    return [
        CaseObject(
            seconds=3, 
            grid=[
                ".......",
                "...O...",
                "....O..",
                ".......",
                "OO.....",
                "OO....."
            ],
            output=[
                "OOO.OOO",
                "OO...OO",
                "OOO...O",
                "..OO.OO",
                "...OOOO",
                "...OOOO"
            ]
        ),
        CaseObject(
            seconds=5, 
            grid=[
                ".......",
                "...O.O.",
                "....O..",
                "..O....",
                "OO...OO",
                "OO.O..."
            ],
            output=[
                ".......",
                "...O.O.",
                "...OO..",
                "..OOOO.",
                "OOOOOOO",
                "OOOOOOO"
            ]
        ),
    ]


def test_code(get_fixtures):
    for test in get_fixtures:
        assert bombaerman_game(test.seconds, test.grid) == test.output
