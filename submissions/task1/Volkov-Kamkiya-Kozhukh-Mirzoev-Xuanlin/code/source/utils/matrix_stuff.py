def delete_dominated_n_equal(matrix, indexes1, indexes2, n, m):
    ''' 
    matrix = list[list[float]]; copy of source_matrix
    indexes1 = list[int]; usable indexes of rows
    indexes2 = list[int]; usable indexes of columns
    n = int: count of strategies of first player
    m = int: count of strategies of second player
    ---------------------------------------------
    Delete dominated strategies, transform to matrix with only positive elements
    '''
    is_any_dominated_strategies = True
    is_any_equal = True
    while is_any_dominated_strategies or is_any_equal:
        is_any_equal = False
        i = 0
        while i < n:
            j = i + 1
            while j < n:
                is_equal = True
                for k in range(0, m):
                    if matrix[i][k] != matrix[j][k]:
                        is_equal = False
                if is_equal:
                    is_any_equal = True
                    matrix.pop(j)
                    indexes1.pop(j)
                    n -= 1
                    j -= 1
                j += 1
            i += 1
        
        i = 0
        while i < m:
            j = i + 1
            while j < m:
                is_equal = True
                for k in range(n):
                    if matrix[k][i] != matrix[k][j]:
                        is_equal = False
                if is_equal:
                    for k in range(n):
                        is_any_equal = True
                        matrix[k].pop(j)
                    indexes2.pop(j)
                    m -= 1
                    j -= 1
                j += 1
            i += 1
        
        dominated_strategies1 = []
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                is_dominated = True
                for k in range(m):
                    if matrix[i][k] > matrix[j][k]:
                        is_dominated = False
                if is_dominated:
                    dominated_strategies1.append(i)
                    break
        count_of_deleted = 0
        for num in dominated_strategies1:
            matrix.pop(num - count_of_deleted)
            indexes1.pop(num - count_of_deleted)
            n -= 1
            count_of_deleted += 1
        
        dominated_strategies2 = []
        for i in range(m):
            for j in range(m):
                if i == j:
                    continue
                is_dominated = True
                for k in range(n):
                    if matrix[k][i] < matrix[k][j]:
                        is_dominated = False
                if is_dominated:
                    dominated_strategies2.append(i)
                    break
        count_of_deleted = 0
        for num in dominated_strategies2:
            for i in range(n):
                matrix[i].pop(num - count_of_deleted)
            indexes2.pop(num - count_of_deleted)
            m -= 1
            count_of_deleted += 1
        
        if len(dominated_strategies1) > 0 or len(dominated_strategies2) > 0:
            is_any_dominated_strategies = True
        else:
            is_any_dominated_strategies = False
