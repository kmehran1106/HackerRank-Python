import pytest
from typing import List


def get_acm_team(array: List[str]) -> List[int]:
    n = len(array)      # total number of people    
    m = len(array[0])   # total number of topics

    max_topics = 0
    num_teams = 0

    b = [ [p[i] == "1" for i in range(m)] for p in array]

    for i in range(n):
        for j in range(i+1, n):
            f = 0
            for x in range(m):
                f = f + 1 if b[i][x] or b[j][x] else f
            if f == max_topics:
                num_teams += 1
            elif f > max_topics:
                num_teams = 1
                max_topics = f
    return [max_topics, num_teams]


@pytest.fixture
def get_fixtures():
    first_input = ["10101", "11100", "11010", "00101"]
    first_output = [5, 2]

    second_input = ["11101", "10101", "11001", "10111", "10000", "01110"]
    second_output = [5, 6]

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert get_acm_team(data[0]) == data[1]


if __name__ == '__main__':
    array = ["10101", "11100", "11010", "00101"]
    get_acm_team(array)