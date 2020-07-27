import pytest
from typing import List


def sock_merchant(array: List[int]) -> int:
    sock_dict = dict()
    pair_count = 0

    for v in array:
        v = str(v)
        if sock_dict.get(v, None):
            sock_dict[v] += 1
        else:
            sock_dict[v] = 1

    for _, v in sock_dict.items():
        pair_count += v//2
    return pair_count


@pytest.fixture
def get_fixtures():
    first_input = [1, 2, 1, 2, 1, 3, 2]
    first_output = 2

    second_input = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    second_output = 3

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert sock_merchant(data[0]) == data[1]