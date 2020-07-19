import pytest

def taum_birthday(b: int, w: int, bc: int, wc: int, z: int) -> int:
    """
    Args:
        b (int): [Number of B gifts]
        w (int): [Number of W gifts]
        bc (int): [Cost of each B gift]
        wc (int): [Cost of each W gift]
        z (int): [Price to convert B to W or W to B]

    Returns:
        int: [Minimum Cost to get Required B&W gifts]
    """
    if bc > wc and z < bc - wc:
        x = w * wc
        y = b * (wc + z)
        return x + y
    elif wc > bc and z < wc - bc:
        x = b * bc
        y = w * (bc + z)
        return x + y
    else:
        return b * bc + w * wc


@pytest.fixture
def get_fixtures():
    first_input = [3, 5, 3, 4, 1]
    first_output = 29

    second_input = [10, 10, 1, 1, 1]
    second_output = 20
    
    third_input = [5, 9, 2, 3, 4]
    third_output = 37

    fourth_input = [3, 6, 9, 1, 1]
    fourth_output = 12

    fifth_input = [7, 7, 4, 2, 1]
    fifth_output = 35

    sixth_input = [3, 3, 1, 9, 2]
    sixth_output = 12

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
        (fourth_input, fourth_output),
        (fifth_input, fifth_output),
        (sixth_input, sixth_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert taum_birthday(*data[0]) == data[1]