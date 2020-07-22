import pytest
from typing import List

import math


def encryption(s: str) -> str:
    l = math.sqrt(len(s))
    r = math.floor(l)
    c = math.ceil(l)

    while r * c < len(s):
        if r < c:
            r += 1
        else:
            c += 1

    array = list()

    for i in range(r):
        first = int(i*c)
        last = int(first + c)
        sub = s[first:last]
        while len(sub) < c:
            sub += " "
        array.append(sub)
    output = ""
    for i in range(c):
        t = ""
        for sub in array:
            t += sub[i]
        t = t.strip()
        output += t + " "
    output = output.strip()
    return output


@pytest.fixture
def get_fixtures():
    first_input = "feedthedog"
    first_output = "fto ehg ee dd"

    second_input = "haveaniceday"
    second_output = "hae and via ecy"

    third_input = "chillout"
    third_output = "clu hlt io"

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert encryption(data[0]) == data[1]


if __name__ == "__main__":
    print(encryption("chillout"))