from builtins import print

import pytest


def modified_kaprekar(p: int, q: int) -> str:
    result = list()
    for num in range(p, q+1):
        d = len(str(num))
        num_squared = str(num * num)
        r = num_squared[-d:]
        l = num_squared.replace(r, "")
        if l == "":
            l = "0"
        if int(r) + int(l) == num:
            result.append(str(num))
    return " ".join(result)
    

@pytest.fixture
def get_fixtures():
    first_input = [1, 100]
    first_output = "1 9 45 55 99"

    second_input = [100, 300]
    second_output = "297"

    third_input = [400, 700]
    third_output = ""

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert modified_kaprekar(*data[0]) == data[1]


if __name__ == "__main__":
    print(modified_kaprekar(400, 700))
