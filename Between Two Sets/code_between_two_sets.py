import pytest
from typing import List


def get_gcd_pair(a: int, b: int) -> int:
    while b > 0:
        temp = b
        b = a % b
        a = temp
    return a


def get_gcd_list(array: List[int]) -> int:
    result = array[0]

    for val in array[1:]:
        result = get_gcd_pair(result, val)
    return result


def get_lcm_pair(a: int, b: int) -> int:
    return a * (b / get_gcd_pair(a, b))


def get_lcm_list(array: List[int]) -> int:
    result = array[0]

    for val in array[1:]:
        result = get_lcm_pair(result, val)
    return result


def between_two_sets(first: List[int], second: List[int]) -> int:
    count = 0

    first.sort()
    second.sort()

    lcm = int(get_lcm_list(first))
    gcd = int(get_gcd_list(second))
    
    i = lcm
    j = 2

    while i <= gcd:
        if gcd % i == 0: 
            count += 1
        i = lcm * j
        j += 1
    return count


@pytest.fixture
def get_fixtures():
    first_input = [
        [2, 4], [16, 32, 96]
    ]
    first_output = 3

    return [
        (first_input, first_output)
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert between_two_sets(*data[0]) == data[1]


def test_get_gcd_pair():
    assert get_gcd_pair(8, 40) == 8
    assert get_gcd_pair(11, 17) == 1
    assert get_gcd_pair(33, 51) == 3


def test_get_gcd_list():
    assert get_gcd_list(array=[8, 40, 160]) == 8


def test_get_lcm_pair():
    assert get_lcm_pair(8, 40) == 40
    assert get_lcm_pair(11, 17) == 187
    assert get_lcm_pair(33, 51) == 561


def test_get_lcm_list():
    assert get_lcm_list(array=[8, 40, 160]) == 160