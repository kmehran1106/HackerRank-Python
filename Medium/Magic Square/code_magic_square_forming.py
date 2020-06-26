import pytest
from typing import List
from copy import deepcopy


def print_matrix(m: List[List[int]]):
    s = ""
    for i in m:
        k = str(i) 
        k = k[1:-1]
        s += f"{k}\n"
    print(s)


def generate_magic_square() -> List[List[int]]:
    """
    [
        The algorithm here is to move to the upper-right of the previous number
        If the space is occupied, insert the number just below the last inserted number
        0 1 0    0 1 0    0 1 0    0 1 0
        0 0 0 -> 0 0 0 -> 3 0 0 -> 3 0 0
        0 0 0    0 0 2    0 0 2    4 0 2
    ]

    Returns:
        List[List[int]]: [Matrix of x*x]
    """
    x = 3
    m = list()
    for i in range(x):
        m.append([0] * x)
    a, b = 0, x//2
    m[a][b] = 1
    for i in range(2, (x*x)+1):
        c = a - 1 if a > 0 else x - 1
        d = b + 1 if b < x - 1 else 0
        if m[c][d] == 0:
            m[c][d] = i
        else:
            c = a + 1
            d = b
            m[c][d] = i
        a, b = c, d
    return m


def rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix) - 1  # max index of the matrix
    for i in range(len(matrix)//2):
        for j in range(i, n - i):
            temp = matrix[i][j]
            # clockwise
            matrix[i][j] = matrix[n-j][i]
            matrix[n-j][i] = matrix[n-i][n-j]
            matrix[n-i][n-j] = matrix[j][n-i]
            matrix[j][n-i] = temp
            # anti-clockwise
            # matrix[i][j] = matrix[j][n-i]
            # matrix[j][n-i] = matrix[n-i][n-j]
            # matrix[n-i][n-j] = matrix[n-j][i]
            # matrix[n-j][i] = temp
    return matrix


def convert_matrix_into_array(matrix: List[List[int]]) -> List[int]:
    t = list()
    for array in matrix:
        for i in array:
            t.append(i)
    return t


def flip_matrix(matrix: List[List[int]]) -> List[List[int]]:
    output = list()
    n = len(matrix) - 1
    for array in matrix:
        output.append(array[::-1])
    return output


def magic_square_forming(matrix: List[List[int]]) -> int:
    g = list()
    magic_square_regular = generate_magic_square()
    magic_square_flipped = flip_matrix(magic_square_regular)
    g.append(convert_matrix_into_array(magic_square_regular))
    g.append(convert_matrix_into_array(magic_square_flipped))
    
    for i in range(3):
        x = rotate_matrix(magic_square_regular)
        y = flip_matrix(x)
        g.append(convert_matrix_into_array(x))
        g.append(convert_matrix_into_array(y))
    
    f = convert_matrix_into_array(matrix)
    r = 99

    for l in g:
        s = 0
        for i, v in enumerate(f):
            s += abs(v-l[i])
        if s < r:
            r = s
    return r


@pytest.fixture
def get_fixtures():
    first_input = [
        [5, 3, 4,],
        [1, 5, 8,],
        [6, 4, 2,],
    ]
    first_output = 7

    return [
        (first_input, first_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert magic_square_forming(data[0]) == data[1]


if __name__ == '__main__':
    g = list()
    magic_square_regular = generate_magic_square()
    magic_square_flipped = flip_matrix(deepcopy(magic_square_regular))
    g.append(convert_matrix_into_array(magic_square_regular))
    g.append(convert_matrix_into_array(magic_square_flipped))
    
    for i in range(3):
        x = rotate_matrix(magic_square_regular)
        y = flip_matrix(deepcopy(x))
        g.append(convert_matrix_into_array(x))
        g.append(convert_matrix_into_array(y))
    print(g)