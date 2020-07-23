import pytest
from typing import Optional

import math


def bigger_is_greater(s: str) -> Optional[str]:
    array = list(s)
    # calculate the suffix
    i = len(array) - 1
    while i > 0 and array[i - 1] >= array[i]:
        i -= 1
    if i <= 0:
        return None
    # get the pivot
    pivot = i - 1

    # get the lowest suffix that is lower than the pivot
    j = len(array) - 1
    while array[j] <= array[pivot]:
        j -= 1

    # swap pivot with lowest suffix
    array[pivot], array[j] = array[j], array[pivot]

    # sort the suffix in ascending order, for this use case we can just reverse it
    array[i:] = array[len(array):pivot:-1]
    return "".join(array)


@pytest.fixture
def get_fixtures():
    first_input = "ab"
    first_output = "ba"

    second_input = "bb"
    second_output = None

    third_input = "hefg"
    third_output = "hegf"

    fourth_input = "dhck"
    fourth_output = "dhkc"

    fifth_input = "dkhc"
    fifth_output = "hcdk"

    sixth_input = "lmno"
    sixth_output = "lmon"

    seventh_input = "dcba"
    seventh_output = None

    eighth_input = "dcbb"
    eighth_output = None

    ninth_input = "abdc"
    ninth_output = "acbd"

    tenth_input = "abcd"
    tenth_output = "abdc"

    eleventh_input = "fedcbabcd"
    eleventh_output = "fedcbabdc"

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
        (fourth_input, fourth_output),
        (fifth_input, fifth_output),
        (sixth_input, sixth_output),
        (seventh_input, seventh_output),
        (eighth_input, eighth_output),
        (ninth_input, ninth_output),
        (tenth_input, tenth_output),
        (eleventh_input, eleventh_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert bigger_is_greater(data[0]) == data[1]


if __name__ == "__main__":
    print(bigger_is_greater("dkhc"))