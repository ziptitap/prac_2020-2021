import numpy as np

def tranform_to_positive(arr):
    plus = 0
    min_elem = arr.min()
    if (min_elem < 0):
        plus = -min_elem + 1
        arr = arr + plus
    return arr,plus


def del_raws_cols (A1, A_help_ind_1):
    A = np.copy(A1)
    A_help_ind = np.copy(A_help_ind_1)
    
    delete_raws_list = []
    delete_cols_list = []
    
    for i in range(A1.shape[0]):
        for j in range(i, A1.shape[0]):
            if np.prod(A[i, :] < A[j, :]) and not (i in set(delete_raws_list)): 
                delete_raws_list.append(i)
            if np.prod(A[i, :] > A[j, :]) and not (j in set(delete_raws_list)):
                delete_raws_list.append(j)
                
    for i in range(A1.shape[1]):
        for j in range(i , A1.shape[1]): 
            if np.prod(A[:, i] > A[:, j]) and not (i in set(delete_cols_list)):
                delete_cols_list.append(i)
            if np.prod(A[:, i] < A[:, j]) and not (j in set(delete_cols_list)):
                delete_cols_list.append(j)            
                
    delete_raws_list.sort(reverse=True)
    delete_cols_list.sort(reverse=True)

    for i in delete_raws_list:
        A = np.delete(A, i, axis=0) 
        A_help_ind = np.delete(A_help_ind, i, axis=0) 
    for i in delete_cols_list:
        A = np.delete(A, i, axis=1)
        A_help_ind = np.delete(A_help_ind, i, axis=1)
    return A, A_help_ind


def del_dominate(A,A_ind):
    A1, A_ind = del_raws_cols(A,A_ind)
    if np.prod(A == A1):
        return A, A_ind
    else:
        return del_dominate(A1,A_ind)