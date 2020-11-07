import numpy as np
from scipy.optimize import linprog
import unittest
def nash_equilibrium(a):
c = [-1 for i in range(0,a.shape[1])]
b = [1 for i in range(0,a.shape[0])]
q = linprog(c, a, b).x
p = linprog(b, -a.transpose(),c).x
opt_sum = 0
for i in p:
opt_sum+=i
cost = 1/opt_sum
return (cost, p*cost, q*cost)
class TestNash(unittest.TestCase):
def test_1(self):
matrix = np.array([
		[3, 1, 2, 5],
		[2, 0, 0, 3],
		[-3, -5, -5, -2],
		[0, -2, -2, 1]
		])
func_cost, func_p, func_q = nash_equilibrium(matrix)
cost = 1
p = np.array([1, 0, 0, 0])
q = np.array([0, 1, 0, 0])
for pair in zip(p.tolist(), func_p.tolist()):
self.assertAlmostEqual(pair[0], pair[1], 5)
for pair in zip(q.tolist(), func_q.tolist()):
self.assertAlmostEqual(pair[0], pair[1], 5)
def test_2(self):
matrix = np.array([
		[7, 6, 0, 8],
		[5, 2, 4, 3],
		[1, 7, 2, 9],
		[9, 0, 2, 5]
		])
func_cost, func_p, func_q = nash_equilibrium(matrix)
cost = 3.42857
p = np.array([0, 0.71429, 0.28571, 0])
q = np.array([0, 0.28571, 0.71429, 0])
for pair in zip(p.tolist(), func_p.tolist()):
self.assertAlmostEqual(pair[0], pair[1], 5)
for pair in zip(q.tolist(), func_q.tolist()):
self.assertAlmostEqual(pair[0], pair[1], 5)
def test_3(self):
matrix = np.array([
		[4, 7, 2],
		[7, 3, 2],
		[2, 1, 8]
		])
func_cost, func_p, func_q = nash_equilibrium(matrix)
cost = 4.02941
p = np.array([0.42647, 0.23529, 0.33824])
q = np.array([0.35294, 0.26471, 0.38235])
for pair in zip(p.tolist(), func_p.tolist()):
self.assertAlmostEqual(pair[0], pair[1], 5)
for pair in zip(q.tolist(), func_q.tolist()):
self.assertAlmostEqual(pair[0], pair[1], 5)
def test_4(self):
matrix = np.array([
		[4, 6, 7, 3, 5],
		[1, 5, 9, 0, 6],
		[7, 0, 0, 1, 8],
		[9, 4, 7, 2, 5]
		])
func_cost, func_p, func_q = nash_equilibrium(matrix)
cost = 3
p = np.array([1, 0, 0, 0])
q = np.array([0, 0, 0, 1, 0])
for pair in zip(p.tolist(), func_p.tolist()):
self.assertAlmostEqual(pair[0], pair[1], 5)
for pair in zip(q.tolist(), func_q.tolist()):
self.assertAlmostEqual(pair[0], pair[1], 5)
def test_5(self):
matrix = np.array([
		[6, 9, 7, 3, 0],
		[1, 7, 3, 9, 5],
		[7, 2, 9, 5, 9],
		[2, 1, 8, 6, 3],
		[9, 0, 5, 2, 7],
		[8, 6, 9, 3, 5],
		[0, 3, 2, 7, 4],
		[8, 2, 1, 9, 7]
		])
func_cost, func_p, func_q = nash_equilibrium(matrix)
cost = 5.59615
p = np.array([0, 0.32692, 0.11538, 0, 0, 0.49038, 0, 0.06731])
q = np.array([0.16346, 0.36538, 0, 0.12981, 0.34135])
for pair in zip(p.tolist(), func_p.tolist()):
self.assertAlmostEqual(pair[0], pair[1], 5)
for pair in zip(q.tolist(), func_q.tolist()):
self.assertAlmostEqual(pair[0], pair[1], 5)
if __name__== '__main__':
unittest.main()
