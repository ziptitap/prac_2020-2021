import easy_solution,transform_matrix,simplex_new, visualize
import numpy as np


# # Вводим матрицу
# Задаём какую-нибудь стандартную для примера работы

matrix = np.array([
    [9, 16, 9, -1],
    [-2, 8, 8, 12],
    [9, 16, -9, 4]])


# # Поиск решения
# ### 1) Есть седловая точка - решение найдено
# ### 2) Рассмотрение общего случая
# 2.1) Преобразуем матрицу к матрице с неотрицательными элементами путём добавления к каждому элементу минимального элемента данной матрицы.
# 
# 2.2)Исключаем доминируемые(щие) стратегии (...)

# ### 2.3) Применяем симплекс метод и находим оптимальные стратегии p_vector и q_vector 

def nash_equilibrium(mat):
    price = 0
    flag, i, j = easy_solution.find_S(matrix)
    if (flag):
        price = matrix[i, j]
        p = matrix[i,:]
        j = matrix[:,j]
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
            if float(i) in A_zero_col_ind_set:
                p_vector[i] = p_cut_vector[j]
                j += 1
        j = 0
        for i in range(matrix.shape[0]):
            if i in A_zero_raw_ind_set:
                q_vector[i] = q_cut_vector[j]
                j += 1
                
    return price, p_vector, q_vector


price, p_vector, q_vector = nash_equilibrium(matrix)


# ## 3) Выводим цену игры, оптимальные стратегии каждого игрока и визуализируем их спектр


print ('Value of a game: %.2f' %  price)

num = 0

print ("\n\np_optim: ", end = "  ") 
visualize.draw_graph(p_vector, 'r', num)  

num += 1

print ("\n\nq_optim: ", end = "  ")   
visualize.draw_graph(q_vector, 'b', num) 

print('\n')