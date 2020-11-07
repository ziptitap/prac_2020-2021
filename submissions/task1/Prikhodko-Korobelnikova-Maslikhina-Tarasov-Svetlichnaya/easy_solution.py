import numpy as np 

def find_S(arr):
    raw = 0
    for i in arr:
        max = np.max(arr, axis = 1)[raw]
        b = np.where(i == max)
        c = arr[:,b]
        for col in b[0]:
            if i[col] == np.min(c):
                return True, raw, col
        raw =+ 1
    return False, -1, -1
