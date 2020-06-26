import pytest
from typing import List


def binary_search(array: List[int], left: int, right: int, x: int) -> int:
    if right >= left:
        mid = (right + left) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binary_search(array, left=left, right=mid-1, x=x)
        elif array[mid] < x:
            return binary_search(array, left=mid+1, right=right, x=x)
        else:
            pass
    else:
        return right

def climbing_leaderboard_binary(scores: List[int], alice: List[int]) -> List[int]:
    scores = sorted(list(set(scores)))
    rank_list = list()
    for i in alice:
        v = binary_search(scores, 0, len(scores)-1, i)
        rank_list.append(len(scores) - v)
    return rank_list 
        

def climbing_leaderboard_iterative(scores: List[int], alice: List[int]) -> List[int]:
    scores = sorted(list(set(scores)))
    index = 0
    rank_list = []
    n = len(scores)
    for i in alice:
        while (n > index and i >= scores[index]):
            index += 1
        rank_list.append(n+1-index) 
    return rank_list


@pytest.fixture
def get_fixtures():
    first_input = [
        [100, 90, 90, 80, 75, 60,],
        [50, 65, 77, 90, 102,],
    ]
    first_output = [6, 5, 4, 2, 1,]

    second_input = [
        [100, 100, 50, 40, 40, 20, 10,],
        [5, 25, 50, 120,],
    ]
    second_output = [6, 4, 2, 1,]

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert climbing_leaderboard_binary(*data[0]) == data[1]
        assert climbing_leaderboard_iterative(*data[0]) == data[1]