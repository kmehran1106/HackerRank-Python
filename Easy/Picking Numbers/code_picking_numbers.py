import pytest

from typing import List


def picking_numbers(array: List[int]) -> int:
    max_len = 0
    hash_map = dict()
    array.sort()
    for var in array:
        x = hash_map.get(var, None)
        if x is None: 
            hash_map[var] = 1
        else:
            hash_map[var] += 1
    for k, v in hash_map.items():
        if v == -1:
            continue
        temp = hash_map.get(k+1, None)
        if temp:
            temp += v
            if temp > max_len: 
                max_len = temp
                hash_map[k] = -1
                hash_map[k+1] = -1
        else:
            temp = v
            if temp > max_len: 
                max_len = temp
            hash_map[k] = -1
    
    return max_len
    

@pytest.fixture
def get_fixtures():
    first_input = [1, 2, 2, 1, 2]
    first_output = 5

    second_input = [1, 2, 2, 3, 1, 2]
    second_output = 5

    third_input = [66, 66, 66, 66, 66, 66]
    third_output = 6

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert picking_numbers(data[0]) == data[1]
