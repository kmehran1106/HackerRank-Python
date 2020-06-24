import pytest


"""
    1. Get Row Combination List given W
        -> [1, 2, 4, 8, 15]
    2. Get Total Walls List Using the RowCombination and H
        -> [1, 2, 4,  8,  15]           if H=1
        -> [1, 4, 16, 64, 225]          if H=2
    
    3. Now, the formula for Solid Wall:
        Total(W, H) - Sum of Non Solid Walls
        How to get Non Solid Walls?
        #   #   *       #   #           *       *
        1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16
        aaa ab- b-a c-- aaa ab- b-a c-- aaa ab- b-a  c-- aaa ab- b-a c--
        aaa aaa aaa aaa ab- ab- ab- ab- b-a b-a b-a  b-a c-- c-- c-- c--  

        Curiously, in 3,9,11 where the breakpoint L=2, we see that,
        LEFT of L = Solid(2, 2)     -> Solid(L, 2)
        RIGHT of L = Total(1, 2)    -> Total(W-L, 2)

        Also for L=1,
        LEFT of L = Solid(1, 2)     -> Solid(L, 2)
        RIGHT of L = Total(2, 2)    -> Total(W-L, 2)

        Quite curious indeed isn't it?
        So total NonSolid for L=1-> Solid(L, 2)*Total(W-L, 2) = 4
        So total NonSolid for L=2-> Solid(L, 2)*Total(W-L, 2) = 3
        Total NonSolid = 7
        That Makes the Total Solid to be 9 which we expect here.
"""


def C(x: int) -> int:
    if x < 0:
        return 0
    elif x == 0:
        return 1
    else:
        return C(x-1) + C(x-2) + C(x-3) + C(x-4)

def get_total_walls(width: int, height: int) -> int:
    return C(width) ** height


def get_solid_walls(width: int, height: int) -> int:
    total = get_total_walls(width, height)

    non_solid_walls = 0

    for l in range(1, width):
        s = get_solid_walls(width-l, height)
        t = get_total_walls(l, height)
        non_solid_walls += (s * t)
    return total - non_solid_walls

@pytest.fixture
def get_total_walls_fixtures():
    first_input = (2, 2)
    first_output = 4

    second_input = (3, 2)
    second_output = 16

    third_input = (2, 3)
    third_output = 8

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
    ]


@pytest.fixture
def get_solid_walls_fixtures():
    # first_input = (529, 190)
    # first_output = 461438538

    second_input = (3, 2)
    second_output = 9

    third_input = (4, 4)
    third_output = 3375


    return [
        # (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
    ]


def test_get_total_walls(get_total_walls_fixtures):
    for data in get_total_walls_fixtures:
        w = data[0][0]
        h = data[0][1]
        assert get_total_walls(w, h) == data[1]


def test_get_solid_walls(get_solid_walls_fixtures):
    for data in get_solid_walls_fixtures:
        w = data[0][0]
        h = data[0][1]
        assert get_solid_walls(w, h) == data[1]