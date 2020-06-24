from os.path import abspath

import pytest

MOD = 10**9 + 7


def get_row_combinations(width: int) -> list:
    f = list()

    f.append(0)
    f.append(1)

    if width > 1: f.append(2)   # w=2
    if width > 2: f.append(4)   # w=3
    if width > 3: f.append(8)   # w=4 
    
    if width > 4:
        for i in range(5, width+1): 
            combination_for_width = (f[i-1] + f[i-2] + f[i-3] + f[i-4]) % MOD
            f.append(combination_for_width)
        # What happens here is that if width = 8, we append the combinations for 
        # width = 5, width = 6, width = 7 and width =  8 in this list
        # we did it recursively in the old code file, but for big numbers the recursion 
        # will take a really long time to complete
    return f


def get_total_walls(c: int, height: int) -> int:
    return c ** height % MOD

def get_solid_walls(width: int, height: int) -> int:
    w = width % MOD
    h = height % MOD
    
    """
    1. Get Row Combination List given W
        -> [1, 2, 4, 8, 15]
    2. Get Total Walls List Using the RowCombination and H
        -> [1, 2, 4,  8,  15]           if H=1
        -> [1, 4, 16, 64, 225]          if H=2
    Now, the formula for Solid Wall:
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
    combination_list = get_row_combinations(w)
    total_walls_list = [get_total_walls(c, h) for c in combination_list]
    
    solid_walls_list = [0] * (w + 1) 
    solid_walls_list[1] = 1

    for i in range(2, (width+1)):
        non_solid_walls = 0
        for j in range(1, i):
            non_solid_walls += solid_walls_list[i-j] * total_walls_list[j]
        solid_walls_list[i] = (total_walls_list[i] - non_solid_walls) % MOD

    return solid_walls_list[-1] % MOD

@pytest.fixture
def get_solid_walls_fixtures():
    first_input = (529, 190)
    first_output = 461438538

    return [
        (first_input, first_output),
    ]


def test_get_solid_walls(get_solid_walls_fixtures):
    for data in get_solid_walls_fixtures:
        w = data[0][0]
        h = data[0][1]
        assert get_solid_walls(w, h) == data[1]