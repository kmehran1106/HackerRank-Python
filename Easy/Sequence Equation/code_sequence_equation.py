import pytest
from typing import List


def sequence_equation(p: List[int]) -> List[int]:
    """
    [
        This is one of the shittiest problems I have faced, with almost no explanation.
        
        p(x)    -> 4 3 5 1 2
          x     -> 1 2 3 4 5
        p(y)    -> 4 5 2 1 3
        p(p(y)) -> 1 3 5 4 2
        for x = 1, p(1) = 4. so we find p(y) for y = 4
    ]

    Args:
        p (List[int]): [description]

    Returns:
        List[int]: [description]
    """
    d = dict()
    x = dict()
    l = list()
    for i, v in enumerate(p):
        d[i+1] = v
    for k, v in d.items():
        x[v] = k
    for i in range(len(p)):
        l.append(x[x[i+1]])
    return l


@pytest.fixture
def get_fixtures():
    first_input = [2, 3, 1,]
    first_output = [2, 3, 1,]

    second_input = [4, 3, 5, 1, 2,]
    second_output = [1, 3, 5, 4, 2,]

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert sequence_equation(data[0]) == data[1]
