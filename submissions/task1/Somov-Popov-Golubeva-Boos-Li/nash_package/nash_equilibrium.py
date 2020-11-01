import numpy as np
from fractions import Fraction 
import matplotlib.pyplot as plt

def add_min_negative(A):  # Избавляемся от отрцательных элементов матрицы, изменится только значение игры.
    m = abs(min(0, min(map(min, A))))
    if m != 0:
        for i in range(len(A)):
            for j in range(len(A[i])):
                A[i][j] += m
        return A, m
    return A, 0 

def table_forming(A):
    m, n = A.shape  # размерность матрицы
    table = np.full((m + 1, n + m + 2), Fraction(0)) #создаём дополнительные строки и столбцы для симплекс-таблицы

    for i in range(m):
        for j in range(n):
            table[i][j] = A[i][j]  # копируем матрицу в таблицу
            
    for i in range(m):
        table[i][i + n] = 1 #значения добавочных переменных
        table[i][-2] = 1  #столбец значений 
        table[i][-1] = i + n + 1  #базис

    for i in range(n):
        table[-1][i] = -1  #в самом начале функция Z равна -1 на основных переменных

    return table


def step(table):
    m, n = table.shape 

    r, c, x = find_rcx(table) 
    for i in range(n-1):
        if x == 0:
            table[r][i] = 0
        else:
            table[r][i] = Fraction(table[r][i], x)
            
    for j in range(m):
        if j == r:
            continue
        mul = table[j][c]
        for i in range(n - 1):
            table[j][i] -= table[r][i] * mul  

    table[r][n - 1] = c + 1 
    return table



def find_rcx(table):  # Ищем строку и столбец
    m, n = table.shape  
    z_max = abs(min(table[-1])) 
    
    c = 0
    for i in range(n):
        if abs(table[-1][i]) == z_max:
            if table[-1][i] < 0:
                c = i
                
    found = False
    for j in range(m - 1):  
        if table[j][c] * table[j][-2] > 0: 
            
            new_val = Fraction(table[j][-2], table[j][c])
            
            if not found:
                found = True
                mtab = new_val
                r = j
            else:
                if new_val < mtab:
                    mtab = new_val
                    r = j

    return r, c, table[r][c]



def optimum(table):
    m, n = table.shape 
    second = np.full((n - m - 1), Fraction(0, 1)) 
    first = np.full((m - 1), Fraction(0, 1))
    
   
    for i in range(m - 1):  
        if table[i][-1] <= n - m - 1:
            second[table[i][-1] - 1] = table[i][-2]

    for i in range(m - 1):  
        first[i] = table[-1][i + n - m - 1]

    return second, first

def simplex(A):
    A, delta = add_min_negative(A)
    
    table = table_forming(A)
    while (table[-1] < 0).any(): 
        table = step(table)

    second, first = optimum(table)
    
    if sum(second) == 0:
        mul = 0
    else:
        mul = Fraction(1, sum(second))
    
    first *= mul
    second *= mul

    return second, first, mul - delta
    
def nash_equilibrium(A):                   
    p = [0] * len(A)
    q = [0] * len(A[0])
    pure = False

    for i in range(len(A)): # ищем седловую точку как нижнее и верхнее значение игры
        game_val = min(A[i])
        index_map = filter(lambda x: A[i][x] == game_val, range(len(A[i])))
        
        
        for j in list(index_map):
            for i in range(len(A)):
                if A[i][j] > game_val:
                    break
            else:
                p[i] = 1
                q[j] = 1
                pure = True
                return p, q, game_val, pure
                
    if not pure:
        p, q, game_val = simplex(A) #если седловой точки нет, ищем решение в смешанных стратегиях
        return p, q, game_val, pure

def spectr(p, name = ''):
    y = p
    x = np.arange(1, np.size(p) + 1)

    fig, ax = plt.subplots()
    
    ax.set_title("Спектры: " + name)
    ax.set_ylabel('Вероятности')
    ax.set_xlabel('Номер стратегии')

    ax.bar(x, y, width = 0.015, color = 'red' )
    ax.plot(x, y, marker='o', linestyle='', color = 'black')
    
def print_result(second, first, p, pure):

    print("Цена игры ", p)

    if not pure:
        print('Оптимальная смешанная стратегия 1 игрока | p | |', end="")
    else:
        print("                 Седловая точка \nПервый игрок  ", end="")

    for i in range(len(first)):
        print(str(first[i]).center(7), end='|')

    print()

    if not pure:
        print('\nОптимальная смешанная стратегия 2 игрока | q | |', end="")
    else:
        print("Второй игрок  ", end="")

    for i in range(len(second)):
        print(str(second[i]).center(7), end='|')
    
    spectr(first, name = "первый игрок")
    spectr(second, name = "второй игрок")

