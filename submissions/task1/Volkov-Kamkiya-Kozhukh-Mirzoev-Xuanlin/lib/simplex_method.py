import sys
'''
structure of simplex-table

Basis       y1    ..., ym, ym+1,..., yn,    value
____________________________________________________
empty(  |coef in | ... |...    |...    |value of
means z)|target f|     |       |       |target f (0)
----------------------------------------------------
index   |coef in |.....|.......|.......|value of
of first|first   |     |       |       |limit
basis   |limit   |     |       |       |
----------------------------------------------------
........|..............................|............
----------------------------------------------------
index   |coef in |.....|.......|.......|value of
of last |last    |     |       |       |limit
basis   |limit   |     |       |       |
____________________________________________________

'''

def checker(simplex_table, deltas, pl_type):
    '''
    simplex_table = list[list[int, (float, ...)]]: prepared simplex_table
    deltas = list[float]: special functions for optimization
    pl_type = int: 0 - first player, 1 - second player
    Checks that all deltas are negative or positive to stop the process
    Returns true if more iterations needed
    '''
    is_any_positive = False
    is_any_negative = False

    for el in deltas:
        if el > 0:
            is_any_positive = True
        if el < 0:
            is_any_negative = True

    if pl_type == 0:
        return is_any_positive
    return is_any_negative


def prepare_simplex(simplex_table):
    '''
    simplex_table = list[list[int, (float, ...)]]: raw simplex_table
    Prepare simplex-table
    '''
    is_any_negative = False

    for i in range(1, len(simplex_table)):
        if simplex_table[i][len(simplex_table[i]) - 1] < 0:
            is_any_negative = True

    while is_any_negative:
        is_any_negative = False
        indx_row = -1
        for i in range(1, len(simplex_table)):
            if simplex_table[i][len(simplex_table[i]) - 1] < 0:
                is_any_negative = True
                if indx_row == -1:
                    indx_row = i
                else:
                    new_mx = abs(simplex_table[i][len(simplex_table[i]) - 1])
                    curr_mx = abs(simplex_table[indx_row][len(simplex_table[indx_row]) - 1])
                    if new_mx > curr_mx:
                        indx_row = i
        if (not is_any_negative):
            break
        
        is_any_negative_in_row = False
        indx_col = -1

        non_basis_variables = []
        for i in range(len(simplex_table[0]) - 2):
            non_basis_variables.append(i + 1)
        
        for i in range(1, len(simplex_table)):
            non_basis_variables.remove(simplex_table[i][0])

        for j in non_basis_variables:
            if simplex_table[indx_row][j] < 0:
                is_any_negative_in_row = True
                curr_mx = abs(simplex_table[indx_row][indx_col])
                new_mx = abs(simplex_table[indx_row][j])
                if new_mx > curr_mx:
                    indx_col = j
        if not is_any_negative_in_row:
            print("Unsolvable")
            sys.exit()
        
        main_el = simplex_table[indx_row][indx_col]
        for j in range(1, len(simplex_table[indx_row])):
            simplex_table[indx_row][j] /= main_el

        for i in range(1, len(simplex_table)):
            if i == indx_row:
                continue
            curr_main_el = simplex_table[i][indx_col]
            for j in range(1, len(simplex_table[i])):
                simplex_table[i][j] -= curr_main_el * simplex_table[indx_row][j]
        
        simplex_table[indx_row][0] = indx_col


def do_simplex(simplex_table, pl_type):
    '''
    simplex_table = list[list[int, (float, ...)]]: prepared simplex_table
    pl_type = int: 0 - first player, 1 - second player
    Does simplex-method
    '''
    len_table = len(simplex_table)
    len_col = len(simplex_table[0])

    deltas = []
    deltas.append(0)
    for j in range(1, len_col - 1):
        delta = 0
        for i in range(1, len_table):
            delta += simplex_table[0][simplex_table[i][0]] * simplex_table[i][j]
        delta -= simplex_table[0][j]
        deltas.append(delta)
    

    while checker(simplex_table, deltas, pl_type):
        indx_col = 1
        for i in range(1, len(deltas)):
            if pl_type == 0:
                if deltas[i] > deltas[indx_col]:
                    indx_col = i
            else:
                if deltas[i] < deltas[indx_col]:
                    indx_col = i
        
        indx_row = -1
        for i in range(1, len_table):
            if simplex_table[i][indx_col] == 0:
                continue
            
            new_min = simplex_table[i][len_col - 1] / simplex_table[i][indx_col]
            is_zero = simplex_table[i][len_col - 1] == 0
            is_negative_zero = is_zero and simplex_table[i][indx_col] < 0
            if new_min < 0 or is_negative_zero:
                continue
            if indx_row == -1:
                indx_row = i
                continue
            
            curr_min = simplex_table[indx_row][len_col - 1] / simplex_table[indx_row][indx_col]
            if new_min < curr_min:
                indx_row = i
        
        incoming_variable = indx_col
        simplex_table[indx_row][0] = incoming_variable

        main_value = simplex_table[indx_row][indx_col]

        for i in range(1, len_col):
            simplex_table[indx_row][i] = simplex_table[indx_row][i] / main_value
        
        for i in range(1, len_table):
            if i == indx_row:
                continue
            curr_main_el = simplex_table[i][indx_col]
            for j in range(1, len_col):
                tmp = curr_main_el * simplex_table[indx_row][j]
                simplex_table[i][j] = simplex_table[i][j] - tmp
        
        deltas = []
        deltas.append(0)
        for j in range(1, len_col - 1):
            delta = 0
            for i in range(1, len_table):
                delta += simplex_table[0][simplex_table[i][0]] * simplex_table[i][j]
            delta -= simplex_table[0][j]
            deltas.append(delta)


def run_simplex(lp_matrix, pl_type):
    '''
    lp_matrix = list[list[float]]: matrix with linear programming task parameters
    pl_type = int: 0 - first player, 1 - second player
    Creates simplex table and run simplex-method.
    Returns result simplex-table
    '''
    simplex_table = []
    cnt_of_rows = len(lp_matrix) + 1
    offset = 0
    sgn = -1.0
    if pl_type:
        sgn *= sgn

    for i in range(cnt_of_rows):
        row = []
        if i == 0:
            row.append(0)
            for j in range(len(lp_matrix[0])):
                row.append(1.0)
            for j in range(len(lp_matrix)):
                row.append(0.0)
            row.append(0.0)
        else:
            row.append(len(lp_matrix[0]) + i)
            for j in range(len(lp_matrix[0])):
                row.append(sgn * lp_matrix[i - 1][j])
            for j in range(offset):
                row.append(0.0)
            row.append(1.0)
            for j in range(len(lp_matrix) - offset - 1):
                row.append(0.0)
            offset += 1
            row.append(sgn)
        simplex_table.append(row)
    
    prepare_simplex(simplex_table)
    do_simplex(simplex_table, pl_type)

    return simplex_table
    