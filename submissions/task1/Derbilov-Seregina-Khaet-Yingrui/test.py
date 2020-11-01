import numpy as np
from scipy.optimize import linprog
from nose.tools import assert_equals
from nash import nash_equil

def nash_equilibrium1(a):
    c = [-1 for i in range(0,a.shape[1])]
    b = [1 for i in range(0,a.shape[0])]
    q = linprog(c, a, b).x
    p = linprog(b, -a.transpose(), c).x
    opt_sum = 0
    for i in p:
        opt_sum += i
    cost = 1 / opt_sum
    return (p * cost, q * cost, cost)

class TestNash:
    def test_1(self): #монетка
        matrix = np.array([
                            [1, -1],
                            [-1, 1]])
        
        #p0, q0, s0 = nash_equilibrium1(matrix)
        p, q, s = nash_equil.nash_equilibrium(matrix)
        s0 = 0
        p0 = np.array([1/2, 1/2])
        q0 = np.array([1/2, 1/2])
        assert_equals(abs(s0 - s) < 0.00001, True)
        assert_equals(sum(abs(x - y) < 0.00001 for x, y in zip(p0, p)), len(p0))
        assert_equals(sum(abs(x - y) < 0.00001 for x, y in zip(q0, q)), len(q0))
    
    def test_2(self): #седло
        matrix = np.array([
                            [1, 1, 1],
                            [1, 2, 3],
                            [4, 5, 6]])
        p0, q0, s0 = nash_equilibrium1(matrix)
        p, q, s = nash_equil.nash_equilibrium(matrix)
        #s = 4
        #p = np.array([0, 0, 1])
        #q = np.array([1, 0, 0])
        assert_equals(abs(s0 - s) < 0.00001, True)
        assert_equals(sum(abs(x - y) < 0.00001 for x, y in zip(p0, p)), len(p0))
        assert_equals(sum(abs(x - y) < 0.00001 for x, y in zip(q0, q)), len(q0))

    def test_3(self):
        matrix = np.array([
                            [0,2,7],
                            [12,11,1]])
        #p0, q0, s0 = nash_equilibrium1(matrix)
        p, q, s = nash_equil.nash_equilibrium(matrix)
        s0 = 14/3
        p0 = np.array([11/18, 7/18])
        q0 = np.array([1/3, 0, 2/3])
        assert_equals(abs(s0 - s) < 0.00001, True)
        assert_equals(sum(abs(x - y) < 0.00001 for x, y in zip(p0, p)), len(p0))
        assert_equals(sum(abs(x - y) < 0.00001 for x, y in zip(q0, q)), len(q0))
        
    def test_4(self):
        matrix = np.array([
                            [1, 4, 6],
                            [7, 2, 1],
                            [5, 3, 2]])
        p0, q0, s0 = nash_equilibrium1(matrix)
        p, q, s = nash_equil.nash_equilibrium(matrix)
        #s = 17/5
        #p = np.array([2/5, 0, 3/5])
        #q = np.array([1/5, 4/5, 0])
        assert_equals(abs(s0 - s) < 0.00001, True)
        assert_equals(sum(abs(x - y) < 0.00001 for x, y in zip(p0, p)), len(p0))
        assert_equals(sum(abs(x - y) < 0.00001 for x, y in zip(q0, q)), len(q0))
        
    def test_5(self):
        matrix = np.array([
                            [4, 7, 2],
                            [7, 3, 2],
                            [2, 1, 8]])
        p0, q0, s0 = nash_equilibrium1(matrix)
        p, q, s = nash_equil.nash_equilibrium(matrix)
        #s = 137/34
        #p = np.array([29/68, 4/17, 23/34])
        #q = np.array([6/17, 9/34, 13/34])
        assert_equals(abs(s0 - s) < 0.00001, True)
        assert_equals(sum(abs(x - y) < 0.00001 for x, y in zip(p0, p)), len(p0))
        assert_equals(sum(abs(x - y) < 0.00001 for x, y in zip(q0, q)), len(q0))

