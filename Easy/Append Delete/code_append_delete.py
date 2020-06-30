import pytest
from typing import List


def append_delete(s: str, t: str, k) -> bool:
    # First find the common length of the two strings
    len_c = 0
    for i in range(0, min(len(s), len(t))):
        if s[i] == t[i]:
            len_c += 1
        else:
            break
    """
    CASE1:
        if len(s) < k - len(t), then we can delete all the letters, 
        keep on going until remaining(k) == len(t), then append len(t)
    CASE2:
        if len(s) + len(t) - 2*common > k,
        then we cannot solve this case
    CASE3:
        if len(s) - common + len(t) - common is ODD, then k must be ODD as well
        if len(s) - common + len(t) - common is EVEN, then k must be EVEN as well
        otherwise, we cannot solve this case
    CASE4:
        NO
    """
    success = True
    if len(s) < k - len(t):
        success = True
    elif len(s) + len(t) - 2*len_c > k:
        success = False
    elif (len(s) + len(t) - 2*len_c) % 2 == k % 2:
        success = True
    else:
        success = False
    return success
    


@pytest.fixture
def get_fixtures():
    first_input = [
        "qwerasdf",
        "qwerbsdf",
        6
    ]
    first_output = False

    second_input = [
        "asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv",
        "bsdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv",
        100
    ]
    second_output = False

    third_input = [
        "hackerhappy",
        "hackerrank",
        9
    ]
    third_output = True

    fourth_input = [
        "aba",
        "aba",
        7
    ]
    fourth_output = True

    fifth_input = [
        "ashley",
        "ash",
        2
    ]
    fifth_output = False
    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
        (fourth_input, fourth_output),
        (fifth_input, fifth_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert append_delete(*data[0]) == data[1]
