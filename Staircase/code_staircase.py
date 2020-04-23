import pytest


def staircase(num: int) -> str:
    output_string = ""
    for i in range(num):
        empty_spaces = " " * (num-1-i)
        hash_values = "#" * (i+1)
        output_string += (empty_spaces + hash_values)
        output_string += "\n"
    output_string = output_string[:-1]
    print(output_string)
    return output_string
    

@pytest.fixture
def get_fixtures():
    first_input = 2
    first_output = " #\n##"

    second_input = 3
    second_output = "  #\n ##\n###"
    return [
        (first_input, first_output),
        (second_input, second_output)
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert staircase(data[0]) == data[1]


if __name__ == "__main__":
    num = int(
        input("Enter Input: ")
    )
    staircase(num)