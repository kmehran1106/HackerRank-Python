import pytest
from typing import List


def non_divisible_subset(array: List[int], k: int) -> int:
    """
    first, we generate an array where the index will be the remainder when an array element is divided by k
    e.g. if array = [4, 5, 6, 7,] and k = 3, then the array will be generated:
    4 % 3 = 1 -> f[1] = 1
    5 % 3 = 2 -> f[2] = 1
    6 % 3 = 0 -> f[0] = 1
    7 % 3 = 1 -> f[1] = 2
    Now, sum of two numbers will be divisible by k, if:
    1. both numbers are divisible by k
    2. if n1%k = i and n2%k = k-i (i.e. i + k - i = k)
    """
    m = k // 2
    f = [0 for i in range(k)]
    for v in array:
        d = v % k
        f[d] += 1
    if k % 2 == 0:
        f[m] = min(f[m], 1)
    r = min(f[0], 1)
    for i in range(1, m+1):
        r += max(f[i], f[k-i])
    return r


@pytest.fixture
def get_fixtures():
    first_input = [
        [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436,], 7
    ]
    first_output = 11

    second_input = [
        [1, 7, 2, 4,], 3
    ]
    second_output = 3

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert non_divisible_subset(*data[0]) == data[1]
