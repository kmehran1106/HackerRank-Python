import pytest
from typing import List


def queens_attack(n: int, k: int, r_q: int, c_q: int, obstacles: List[List[int]]) -> int:
    """
    Args:
        n (int): [Chessboard Size Number. The Board will be nxn]
        k (int): [Number of obstacles on Chessboard.]
        r_q (int): [Row Number of Queen Position]
        c_q (int): [Column Number of Queen Position]
        obstacles (List[List[int]]): [Array of Int Arrays denoting Obstacles Position]

    Returns:
        int: [Number of Places in the Board the Queen can Move to]
    """
    obstacle_map = {f"{i[0]}_{i[1]}": True for i in obstacles}
    result = 0

    # calculate top and bottom
    i, j = r_q, c_q
    while i < n:
        if not obstacle_map.get(f"{i+1}_{j}", None):
            result += 1
            i += 1 
        else:
            break
    print(f"Result After Top: {result}")
    i, j = r_q, c_q
    while i > 1:
        if not obstacle_map.get(f"{i-1}_{j}", None):
            result += 1
            i -= 1 
        else:
            break
    print(f"Result After Bottom: {result}")

    # calculate right and left
    i, j = r_q, c_q
    while j < n:
        if not obstacle_map.get(f"{i}_{j+1}", None):
            result += 1
            j += 1 
        else:
            break
        
    print(f"Result After Right: {result}")
    i, j = r_q, c_q
    while j > 1:
        if not obstacle_map.get(f"{i}_{j-1}", None):
            result += 1
            j -= 1 
        else:
            break
    print(f"Result After Left: {result}")
    
    # calculate diagonals
    i, j = r_q, c_q
    while i < n and j < n:
        if not obstacle_map.get(f"{i+1}_{j+1}", None):
            result += 1
            i += 1 
            j += 1
        else:
            break
    print(f"Result After Top-Right: {result}")
    
    i, j = r_q, c_q
    while i < n and j > 1:
        if not obstacle_map.get(f"{i+1}_{j-1}", None):
            result += 1
            i += 1 
            j -= 1
        else:
            break
    print(f"Result After Top-Left: {result}")

    i, j = r_q, c_q
    while i > 1 and j > 1:
        if not obstacle_map.get(f"{i-1}_{j-1}", None):
            result += 1
            i -= 1 
            j -= 1
        else:
            break
    print(f"Result After Bot-Left: {result}")

    i, j = r_q, c_q
    while i > 1 and j < n:
        if not obstacle_map.get(f"{i-1}_{j+1}", None):
            result += 1
            i -= 1 
            j += 1
        else:
            break
    print(f"Result After Bot-Right: {result}")
    return result


@pytest.fixture
def get_fixtures():
    first_input = [
        4, 0, 4, 4, []
    ]
    first_output = 9

    second_input = [
        5, 3, 4, 3, [ [5, 5,], [4, 2,], [2, 3,] ]
    ]
    second_output = 10

    third_input = [
        1, 0, 1, 1, []
    ]
    third_output = 0

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert queens_attack(*data[0]) == data[1]


if __name__ == "__main__":
    input_data = [
        5, 3, 4, 3, [ [5, 5,], [4, 2,], [2, 3,] ]
    ]
    print(queens_attack(*input_data))
