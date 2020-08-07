import pytest
from typing import List
import math


def get_flatland_space_stations(n: int, array: List[int]) -> int:
    array.sort()

    # distance between first city and first space station
    first_distance = array[0]

    # distance between last city and last space station
    last_distance = n - 1 - array[-1]

    max_distance = first_distance if first_distance > last_distance else last_distance
    # loop through the distances between the intermediary space stations
    # find the max medium distance between each pair and the city between them
    for i in range(1, len(array)):
        d = (array[i] - array[i-1]) // 2
        if d > max_distance:
            max_distance = d
    return max_distance


class CaseObject:
    def __init__(self, n: int, array: List[int], output: int):
        self.n, self.array = n, array
        self.output = output


@pytest.fixture
def get_fixtures():
    return [
        CaseObject(5, [0, 4], output=2),
        CaseObject(6, [0, 1, 2, 3, 4, 5], output=0),
    ]


def test_code(get_fixtures):
    for test in get_fixtures:
        assert get_flatland_space_stations(test.n, test.array) == test.output
