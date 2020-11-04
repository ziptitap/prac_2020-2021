import pytest

import source.matrix_game_solver


def is_equal_matrix(matrix_a, matrix_b):
    eps = 1e-05

    assert len(matrix_a) == len(matrix_b)
    assert len(matrix_a[0]) == len(matrix_b[0])
    for i in range(0, len(matrix_a)):
        assert matrix_a[i][0] == matrix_b[i][0]
    for i in range(0, len(matrix_a[0])):
        assert matrix_a[0][i] == matrix_b[0][i]
    
    for i in range(1, len(matrix_a)):
        for j in range(1, len(matrix_a[0])):
            assert matrix_a[i][j] - matrix_b[i][j] < eps

@pytest.mark.parametrize(
    "matrix, indexes1, indexes2, n, m, enable_rows_and_columns_elimination, ans, res_min_el, indx1, indx2",
    [
        (
            [
                [1, 2, 3],
                [1, 2, 3],
                [1, 3, -1],
            ],
            [0, 1, 2],
            [0, 1, 2],
            3,
            3,
            0,
            [
                [2, 3, 4],
                [2, 3, 4],
                [2, 4, 0],
            ],
            -1,
            [0, 1, 2],
            [0, 1, 2],
        ),
        (
            [
                [1, 2, 3],
                [1, 2, 3],
                [1, 3, -1],
            ],
            [0, 1, 2],
            [0, 1, 2],
            3,
            3,
            1,
            [
                [1],
            ],
            0,
            [0],
            [0],
        ),
        (
            [
                [2, 3, 4],
                [2, 3, 4],
                [1, 3, 5],
            ],
            [0, 1, 2],
            [0, 1, 2],
            3,
            3,
            0,
            [
                [2, 3, 4],
                [2, 3, 4],
                [1, 3, 5],
            ],
            0,
            [0, 1, 2],
            [0, 1, 2],
        ),
    ]
)
def test_prepare_matrix(
    matrix, indexes1, indexes2, n, m, enable_rows_and_columns_elimination, 
    ans, res_min_el, indx1, indx2
    ):
    min_el = source.matrix_game_solver.prepare_matrix(
        matrix, indexes1, indexes2, n, m, enable_rows_and_columns_elimination
    )
    assert matrix == ans
    assert min_el == res_min_el
    assert indexes1 == indx1
    assert indexes2 == indx2

@pytest.mark.parametrize(
    "matrix, n, m, pl_type, ans",
    [
        (
            [
                [1., 4., 6.],
                [7., 2., 0.],
                [5., 3., 2.],
            ],
            3,
            3,
            0,
            [
                [0, 1, 1, 1, 0, 0, 0, 0],
                [3, 0., 26/17, 1., -4/17, 1/17, 0., 3/17],
                [6, 0., -14/17, 0., 10/17, -28/17, 1., 1/17],
                [1, 1., -11/17, 0., 3/17, -5/17, 0., 2/17],
            ],
        ),
        (
            [
                [1., 4., 6.],
                [7., 2., 0.],
                [5., 3., 2.],
            ],
            3,
            3,
            1,
            [
                [0, 1, 1, 1, 0, 0, 0, 0],
                [5, 0., 0., 14/17, 11/17, 1., -26/17, 2/17],
                [1, 1., 0., -10/17, -3/17, 0., 4/17, 1/17],
                [2, 0., 1., 28/17, 5/17, 0., -1/17, 4/17],
            ],
        ),
        
    ],
)
def test_get_simplex(matrix, n, m, pl_type, ans):
    simplex_table = source.matrix_game_solver.get_simplex(matrix, n, m, pl_type)
    is_equal_matrix(simplex_table, ans)
