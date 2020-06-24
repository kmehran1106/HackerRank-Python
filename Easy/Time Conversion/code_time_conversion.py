import pytest


def time_conversion(string: str) -> str:
    last = string[-2:]
    first = string[:2]

    if last == "PM" and int(first) < 12:
        new_first = str(int(first) + 12)
    elif last == "AM" and int(first) == 12:
        new_first = "00"
    else:
        new_first = first
    string = string.replace(first, new_first).replace("PM", "").replace("AM", "")
    return string
    

@pytest.fixture
def get_fixtures():
    first_input = "12:05:00AM"
    first_output = "00:05:00"

    second_input = "12:55:32PM"
    second_output = "12:55:32"

    third_input = "04:00:00AM"
    third_output = "04:00:00"

    fourth_input = "03:21:33PM"
    fourth_output = "15:21:33"

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
        (fourth_input, fourth_output)
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert time_conversion(data[0]) == data[1]


if __name__ == "__main__":
    num = int(
        input("Enter Input: ")
    )
    time_conversion(num)