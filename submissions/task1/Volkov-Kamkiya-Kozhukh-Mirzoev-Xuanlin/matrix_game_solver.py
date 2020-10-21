import sys

import lib.simplex_method
import utils.matrix_stuff


def source_input():
    ''' 
    Prints start information, read source data.
    Returns matrix, count of rows and columns
    '''
    print("********************************************************")
    print("Input source data")
    try:
        N = int(input("Count of strategies of 1 player: "))
        M = int(input("Count of strategies of 2 player: "))
        print("Enter the game matrix:")
        matrix = []
    
        i = 0
        while i < N:
            row = input().split()
            assert len(row) == M
            matrix.append([float(j) for j in row])
            i += 1
    except AssertionError:
        print("Wrong count of column")
        sys.exit()
    except ValueError:
        print("Wrong type of value")
        sys.exit()
    return N, M, matrix


def prepare_matrix(matrix, indexes1, indexes2, n, m, enable_rows_and_columns_elimination = 0):
    ''' 
    matrix = list[list[float]]; copy of source_matrix
    indexes1 = list[int]; usable indexes of rows
    indexes2 = list[int]; usable indexes of columns
    n = int: count of strategies of first player
    m = int: count of strategies of second player
    enable_rows_and_columns_elimination = bool: 
        enables dominated or equal rows and columns elimination
    ---------------------------------------------
    Delete dominated strategies, transform to matrix with only positive elements.
    Returns the value of minimal element in matrix
    '''
    
    if (enable_rows_and_columns_elimination):
        utils.matrix_stuff.delete_dominated_n_equal(matrix, indexes1, indexes2, n, m)
    
    n = len(matrix)
    m = len(matrix[0])

    min_el = matrix[0][0]
    is_any_negative = False

    for i in range(n):
      for j in range(m):
          if matrix[i][j] < 0:
              is_any_negative = True
          min_el = min(min_el, matrix[i][j])
    
    if is_any_negative:
        for i in range(n):
            for j in range(m):
                matrix[i][j] -= min_el

    return min_el


def get_simplex(matrix, n, m):
    '''
    matrix = list[list[float]]: modified matrix of game
    n = int: count of rows
    m = int: count of columns
    Cast modified matrix of game to linear programming task and run simplex-method.
    Returns result simplex-table
    '''
    lp_matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(matrix[j][i])
        lp_matrix.append(row)
    
    return lib.simplex_method.run_simplex(lp_matrix)


def main():
    ''' 
    main function
    '''
    source_n, source_m, source_matrix = source_input()
    matrix = source_matrix.copy()
    n, m = source_n, source_m
    
    indexes1 = []
    for i in range(n):
        indexes1.append(i)
    
    indexes2 = []
    for i in range(m):
        indexes2.append(i)
    
    min_el = prepare_matrix(matrix, indexes1, indexes2, n, m, 1)
    
    n = len(matrix)
    m = len(matrix[0])

    simplex_matrix = get_simplex(matrix, n, m)
    
    target_f = 0
    target_plan = [0] * (len(simplex_matrix[0]) - 2)
    for i in range(1, len(simplex_matrix)):
        curr_value = simplex_matrix[i][len(simplex_matrix[i]) - 1]
        target_plan[simplex_matrix[i][0] - 1] = curr_value
        target_f += curr_value * simplex_matrix[0][simplex_matrix[i][0]]
    
    V = 1/target_f
    print("Target F = {}".format(target_f))
    print("Then V = {}".format(V))
    
    if min_el != 0:
        V = 1/target_f - min_el
        print("Source matrix was modified by adding min_el = {}".format(min_el))
        print("V = V' - min_el = {}".format(V))
    
    first_player_tactics = []
    it = 0
    for i in range(len(source_matrix)):
        if i == indexes1[it]:
            first_player_tactics.append(target_plan[it] * V)
            it += 1
        else:
            first_player_tactics.append(0)
    
    print("First player tactics: {}".format(first_player_tactics))
    
