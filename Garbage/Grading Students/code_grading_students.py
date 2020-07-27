import pytest


def grading_students(array: list) -> list:
    result = list()

    for grade in array:
        mod_by_5 = grade % 5

        if mod_by_5 < 3 or grade < 38:
            result.append(grade)
        else:
            result.append(grade+5-mod_by_5)

    return result


@pytest.fixture
def get_fixtures():
    first_input = [71, 72, 73, 74, 75, 33, 38, 37]
    first_output = (71, 72, 75, 75, 75, 33, 40, 37)

    return [
        (first_input, first_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert all(
            [
                a == b for a, b in zip(grading_students(data[0]), data[1])
            ]
        )
