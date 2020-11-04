import pytest

import lib.simplex_method

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
    "simplex_table, deltas, pl_type, ans",
    [
        (
            [
                [0, 1, 1, 0, 0, 0, 0],
                [3, -5., -3., 1., 0., 0., -1.],
                [4, -2., -4., 0., 1., 0., -1.],
                [5, -7., -1., 0., 0., 1., -1.],
            ],
            [0, -1., -2., -3., -4., -5.],
            0,
            False,
        ),
        (
            [
                [0, 1, 1, 0, 0, 0, 0],
                [3, -5., -3., 1., 0., 0., -1.],
                [4, -2., -4., 0., 1., 0., -1.],
                [5, -7., -1., 0., 0., 1., -1.],
            ],
            [0, 1., -2., -3., -4., -5.],
            0,
            True,
        ),
        (
            [
                [0, 1, 1, 0, 0, 0, 0],
                [3, 5., 3., 1., 0., 0., 1.],
                [4, 2., 4., 0., 1., 0., 1.],
                [5, 7., 1., 0., 0., 1., 1.],
            ],
            [0, 1., 2., 3., 4., 5.],
            1,
            False,
        ),
        (
            [
                [0, 1, 1, 0, 0, 0, 0],
                [3, 5., 3., 1., 0., 0., 1.],
                [4, 2., 4., 0., 1., 0., 1.],
                [5, 7., 1., 0., 0., 1., 1.],
            ],
            [0, -1., 2., 3., 4., 5.],
            1,
            True,
        ),
    ],
)
def test_checker(simplex_table, deltas, pl_type, ans):
    res = lib.simplex_method.checker(simplex_table, deltas, pl_type)
    assert res == ans

@pytest.mark.parametrize(
    "simplex_table, ans",
    [
        (
            [
                [0, 1, 1, 1, 0, 0, 0, 0],
                [4, -1., -7., -5., 1., 0., 0., -1.],
                [5, -4., -2., -3., 0., 1., 0., -1.],
                [6, -6., 0., -2., 0., 0., 1., -1.],
            ],
            [
                [0, 1, 1, 1, 0, 0, 0, 0],
                [2, 0., 1., 17/26, -2/13, 1/26, 0., 3/26],
                [6, 0., 0., 7/13, 6/13, -21/13, 1., 2/13],
                [1, 1., 0., 11/26, 1/13, -7/26, 0., 5/26],
            ],
        ),
        (
            [
                [0, 1, 1, 1, 0, 0, 0, 0],
                [4, 1., 4., 6., 1., 0., 0., 1.],
                [5, 7., 2., 0., 0., 1., 0., 1.],
                [6, 5., 3., 2., 0., 0., 1., 1.],
            ],
            [
                [0, 1, 1, 1, 0, 0, 0, 0],
                [4, 1., 4., 6., 1., 0., 0., 1.],
                [5, 7., 2., 0., 0., 1., 0., 1.],
                [6, 5., 3., 2., 0., 0., 1., 1.],
            ],
        ),
        
    ],
)
def test_prepare_simplex(simplex_table, ans):
    lib.simplex_method.prepare_simplex(simplex_table)
    is_equal_matrix(simplex_table, ans)
    
@pytest.mark.parametrize(
    "simplex_table, pl_type, ans",
    [
        (
            [
                [0, 1, 1, 1, 0, 0, 0, 0],
                [2, 0., 1., 17/26, -2/13, 1/26, 0., 3/26],
                [6, 0., 0., 7/13, 6/13, -21/13, 1., 2/13],
                [1, 1., 0., 11/26, 1/13, -7/26, 0., 5/26],
            ],
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
                [0, 1, 1, 1, 0, 0, 0, 0],
                [4, 1., 4., 6., 1., 0., 0., 1.],
                [5, 7., 2., 0., 0., 1., 0., 1.],
                [6, 5., 3., 2., 0., 0., 1., 1.],
            ],
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
def test_do_simplex(simplex_table, pl_type, ans):
    lib.simplex_method.do_simplex(simplex_table, pl_type)
    is_equal_matrix(simplex_table, ans)

@pytest.mark.parametrize(
    "lp_matrix, pl_type, ans",
    [
        (
            [
                [1., 7., 5.],
                [4., 2., 3.],
                [6., 0., 2.],
            ],
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
def test_run_simplex(lp_matrix, pl_type, ans):
    simplex_table = lib.simplex_method.run_simplex(lp_matrix, pl_type)
    is_equal_matrix(simplex_table, ans)
