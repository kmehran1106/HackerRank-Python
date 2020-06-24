import pytest
from typing import List


def get_programmers_day(year: int) -> str:
    if year < 1918 and year % 4 == 0:
        is_leap = True
    elif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        is_leap = True
    else:
        is_leap = False
    
    month = 9
    base_days = 243 if year != 1918 else 243 - 13
    count_days = 255 if is_leap else 256
    day = count_days - base_days
    
    return str(day) + ".09." + str(year)

    
@pytest.fixture
def get_fixtures():
    first_input = 2017
    first_output = "13.09.2017"

    second_input = 2016
    second_output = "12.09.2016"

    third_input = 1800
    third_output = "12.09.1800"

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert get_programmers_day(data[0]) == data[1]