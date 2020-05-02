import pytest


def counting_valleys(steps: str) -> int:
    count = 0
    in_valley = False
    height = 0
    
    for c in steps:
        height = height - 1 if c == "D" else height + 1
        if height < 0 and not in_valley:
            count += 1
            in_valley = True
        if height >= 0 and in_valley:
            in_valley = False
    return count
    

@pytest.fixture
def get_fixtures():
    first_input = "UDDDUDUU"
    first_output = 1

    second_input = "DDUUDDUDUUUD"
    second_output = 2

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert counting_valleys(data[0]) == data[1]
