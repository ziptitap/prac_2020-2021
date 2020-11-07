import numpy as np 
import easy_solution,transform_matrix,simplex_new, visualize

def nash_equilibrium(matrix, price):
    flag, i, j = easy_solution.find_S(matrix)
    if (flag):
        price = matrix[i, j]
        p_vector = matrix[i,:]
        q_vector = matrix[:,j]
    else:
        A, plus = transform_matrix.tranform_to_positive(matrix)
        A_help_ind = np.zeros((A.shape[0], A.shape[1], 2))

        for i in range(A.shape[0]):
            for j in range(A.shape[1]):
                ind = np.array([i,j])
                A_help_ind[i][j] = ind  
                
                
        A, A_zero_ind = transform_matrix.del_dominate(A,A_help_ind)
        p_cut_vector, q_cut_vector, price = simplex_new.simplex(A, plus)
        A_zero_col_ind_set = {A_zero_ind[0][i][1] for i in range(A_zero_ind.shape[1])}
        A_zero_raw_ind_set = {A_zero_ind[i][0][0] for i in range(A_zero_ind.shape[0])}
        
        p_vector = np.zeros(matrix.shape[1])
        q_vector = np.zeros(matrix.shape[0])
        j = 0
        for i in range(matrix.shape[1]):
            if float(i) in A_zero_raw_ind_set:
                p_vector[i] = p_cut_vector[j]
                j += 1
        j = 0
        for i in range(matrix.shape[0]):
            if i in A_zero_col_ind_set:
                q_vector[i] = q_cut_vector[j]
                j += 1
    p_vector = np.round(p_vector, 2)
    q_vector = np.round(q_vector, 2)
    price = round(price, 2)
    return price, p_vector, q_vector