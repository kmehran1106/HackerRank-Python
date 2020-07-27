import pytest


def cats_and_mouse(cat_a: int, cat_b: int, mouse_c:int) -> str:
    x = abs(cat_a - mouse_c)
    y = abs(cat_b - mouse_c)
    return "Cat A" if x < y else "Cat B" if y < x else "Mouse C"
    

@pytest.fixture
def get_fixtures():
    first_input = [1, 2, 3]
    first_output = "Cat B"

    second_input = [1, 3, 2]
    second_output = "Mouse C"

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert cats_and_mouse(*data[0]) == data[1]
