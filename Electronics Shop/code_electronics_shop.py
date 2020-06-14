import pytest
import math
from typing import List


def electronics_shop(budget: int, keyboards: List[int], drives: List[int]) -> int:
    keyboards = list(filter(lambda x: x < budget, keyboards))
    drives = list(filter(lambda x: x < budget, drives))

    keyboards.sort(reverse=True)
    drives.sort()
    
    cur_max = -1
    for k in keyboards:
        for d in drives:
            print(f"K = {k}; D = {d}")
            if k + d > budget:
                break
            if k + d > cur_max:
                cur_max = k + d
    return cur_max

@pytest.fixture
def get_fixtures():
    first_input = [5, [3, 1], [5, 2, 8]]
    first_output = 5

    second_input = [5, [4], [5]]
    second_output = -1

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert electronics_shop(*data[0]) == data[1]

if __name__ == "__main__":
    electronics_shop(5, [3, 1], [1, 2, 1])