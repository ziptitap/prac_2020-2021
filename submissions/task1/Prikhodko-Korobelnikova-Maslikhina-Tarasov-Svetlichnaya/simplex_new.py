import numpy as np

#нахождение разрешающего столбца в матрице, т.е. минимального отриц. элемента в 0 строке
def find_leading_col(A): 
    leading_col = 1
    minim_elem = A[0][leading_col]
    for j in range(1, A.shape[1]): #цикл по столбцам
        if A[0][j] < minim_elem:
            minim_elem = A[0][j]
            leading_col = j
    if minim_elem >= 0:
        return -1  #т.е. минимальный элемент положительный
    return leading_col


#находим разрешающую строку 
#в каждой строке элемент первого столбца делится на соответствующий элемент разрешающего столбца
#так получается столбец симплекс-отношений
#минимальный элемент в этом столбце и определяет разрешающую строку
def find_leading_row(A, leading_col): 
    leading_row = 0
    min_coefficient = -1.0
    for i in range(1, A.shape[0]):#цикл по строкам
    #делим на лидирующий столбец
        coefficient = A[i][0] / A[i][leading_col]
        if (((coefficient > 0) and (coefficient < min_coefficient)) or (min_coefficient < 0)):
            min_coefficient = coefficient
            leading_row = i
    if min_coefficient < 0:
        return -1 
    return leading_row

def simplex_table(A):     
    r = np.vstack(( np.zeros(A.shape[0]), np.eye(A.shape[0]) ))  
    b = np.array([1,]*(A.shape[0]+1)).reshape(A.shape[0]+1, -1) 
    b[0][0] = 0
    c = np.array([-1, ] * A.shape[1]) #строка из -1
    A = np.vstack((c, A)) 
    A = np.hstack((b, A)) 
    A = np.hstack((A, r)) 
    return A

def transform_simplex_table(A, row, col):
    leading_elem = A[row][col]
    for j in range(A.shape[1]): #цикл по столбцам, делим на лидирующий элемент
        A[row][j] /= leading_elem #делим на лидирующий элемент
    for i in range(A.shape[0]): #гаусс
        if i == row:
            continue
        s = A[i][col]
        for j in range(A.shape[1]):
            A[i][j] -= s*A[row][j]

#ищем базис:только одна координата вектора ненулевая и равна 1. 
#Базисный вектор имеет размерность (m*1), где m – количество уравнений в системе ограничений.     
def find_basis_variable(A, col):
    x_i = -1
    for i in range(1, A.shape[0]): #цикл по строкам и фиксированному столбцу
        if A[i][col] == 1:
            if x_i == -1:
                x_i = i
            else:
                return -1
        else:
            if A[i][col] != 0:
                return -1
    return x_i #номер ненулевого элемента в базисе


def optimal_strategy(A, b):
    p = []
    q = []
    for j in range(1, A.shape[1]):
        x_i = find_basis_variable(A, j)
        if x_i != -1:
            if j < (A.shape[1]-A.shape[0]+1):
                q.append(A[x_i][0])
            else:
                p.append(A[0][j])
        else:
            if j < (A.shape[1]-A.shape[0]+1):
                q.append(0)
            else:
                p.append(A[0][j])
    sum1 = sum(p)
    sum2 = sum(q)
    for i in range(len(p)):
        p[i] /= sum1
    for i in range(len(q)):
        q[i] /= sum2
    return p, q, 1 / sum1 - b


def simplex(a, plus):
    num_of_iterations = 1
    a = simplex_table(a)
    while num_of_iterations:
        leading_col = find_leading_col(a)
        if leading_col < 0: #нулевая строка>0
            p_vector, q_vector, price = optimal_strategy(a, plus)
            return p_vector, q_vector, price
        leading_row = find_leading_row(a, leading_col)
        if leading_row < 0:
            print('no leading row')
            break
        transform_simplex_table (a, leading_row, leading_col)
        num_of_iterations += 1

        
        
        
        
        
        
        
        
        
        
        
        
        
