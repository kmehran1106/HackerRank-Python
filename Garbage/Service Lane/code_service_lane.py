import pytest
from typing import List


def service_lane(width_array: List[int], lower_index: int, upper_index: int) -> int:
    return min(width_array[lower_index:upper_index+1])


class CaseObject:
    def __init__(self, width_array: List[int], lower_index: int, upper_index: int, output: int):
        self.width_array, self.lower_index, self.upper_index = width_array, lower_index, upper_index
        self.output = output


@pytest.fixture
def get_fixtures():
    return [
        CaseObject([2, 3, 1, 2, 3, 2, 3, 3,], 0, 3, output=1),
        CaseObject([2, 3, 1, 2, 3, 2, 3, 3,], 4, 6, output=2),
        CaseObject([2, 3, 1, 2, 3, 2, 3, 3,], 6, 7, output=3),
        CaseObject([2, 3, 1, 2, 3, 2, 3, 3,], 3, 5, output=2),
        CaseObject([2, 3, 1, 2, 3, 2, 3, 3,], 0, 7, output=1),
        CaseObject([1, 2, 2, 2, 1,], 2, 3, output=2),
        CaseObject([1, 2, 2, 2, 1,], 1, 4, output=1),
        CaseObject([1, 2, 2, 2, 1,], 2, 4, output=1),
    ]


def test_code(get_fixtures):
    for test in get_fixtures:
        assert service_lane(test.width_array, test.lower_index, test.upper_index) == test.output
