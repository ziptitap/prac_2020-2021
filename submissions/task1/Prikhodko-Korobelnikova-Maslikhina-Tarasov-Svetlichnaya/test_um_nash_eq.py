import numpy as np
import nash_equilibrium
import easy_solution,transform_matrix,simplex_new, visualize
import unittest

class Test_nash_equilibrium(unittest.TestCase):
    def test_n1(self):
        matrix11 = np.array([
    [9, 16, 9, -1],
    [-2, 8, 8, 12],
    [9, 16, -9, 4]])
        price1, p_vector1, q_vector1 = nash_equilibrium.nash_equilibrium(matrix11, 0)
        self.assertEqual(price1, 4.42)  
        np.testing.assert_equal(p_vector1, np.array([0.58, 0.42, 0.00, 0.00]))
        np.testing.assert_equal(q_vector1, np.array([0.54, 0.00, 0.00]))
        
    def test_n2(self):
        matrix22 = np.array([
    [7, -1, -4, 1],
    [4, 2, 3, 2],
    [2, 2, 5, 2],
    [4, -3, 7, -2]])
        price2, p_vector2, q_vector2 = nash_equilibrium.nash_equilibrium(matrix22, 0)
        self.assertEqual(price2, 2.00)  
        np.testing.assert_equal(p_vector2, np.array([0.00,  1.00,  0.00,  0.00]))
        np.testing.assert_equal(q_vector2, np.array([0.00,  1.00,  0.00,  0.00]))
        
    def test_n3(self):
        matrix33 = np.array([
    [6, 10],
    [12, 3]])
        price3, p_vector3, q_vector3 = nash_equilibrium.nash_equilibrium(matrix33, 0)
        self.assertEqual(price3, 7.85)  
        np.testing.assert_equal(p_vector3, np.array([0.69,  0.31]))
        np.testing.assert_equal(q_vector3, np.array([0.54,  0.46]))
        
    def test_n4(self):
        matrix44 = np.array([
    [4, 0, 6, 2, 2, 1],
    [3, 8, 4, 10, 4, 4],
    [1, 2, 6, 5, 0, 0],
    [6, 6, 4, 4, 10, 3],
    [10, 4, 6, 4, 0, 9],
    [10, 7, 0, 7, 9, 8]])
        price4, p_vector4, q_vector4 = nash_equilibrium.nash_equilibrium(matrix44, 0)
        self.assertEqual(price4, 4.87)  
        np.testing.assert_equal(p_vector4, np.array([0.00,  0.13,  0.10,  0.44, 0.34, 0.00]))
        np.testing.assert_equal(q_vector4, np.array([0.00, 0.00,  0.69, 0.15, 0.15, 0.02]))
        
    def test_n5(self):
        matrix55 = np.array([
    [8, 6, 1],
    [12, 9, 8],
    [14, 5, 1]])
        price5, p_vector5, q_vector5 = nash_equilibrium.nash_equilibrium(matrix55, 0)
        self.assertEqual(price5, 8.00)  
        np.testing.assert_equal(p_vector5, np.array([8.00,  6.00,  1.00]))
        np.testing.assert_equal(q_vector5, np.array([8.00, 12.00,  14.00]))
        
    def test_n6(self):
        matrix66 =  np.array([
    [9, 16, 9, 1],
    [2, 8, 8, 12],
    [9, 16, 9, 4]])
        price6, p_vector6, q_vector6 = nash_equilibrium.nash_equilibrium(matrix66, 0)
        self.assertEqual(price6, 5.89)  
        np.testing.assert_equal(p_vector6, np.array([0.56,  0.44,  0.00, 0.00]))
        np.testing.assert_equal(q_vector6, np.array([0.61, 0.00,  0.00]))

    def test_n7(self):
        matrix77 = np.array([
    [8, -6, -1],
    [12, 9, 8],
    [14, 5, 1]])
        price7, p_vector7, q_vector7 = nash_equilibrium.nash_equilibrium(matrix77, 0)
        self.assertEqual(price7, 8.00)  
        np.testing.assert_equal(p_vector7, np.array([8.00,  -6.00,  -1.00]))
        np.testing.assert_equal(q_vector7, np.array([8.00, 12.00,  14.00]))
        
    def test_n8(self):
        matrix88 = np.array([
    [4, 0, -6, 2, 2, 1],
    [3, 8, 4, -10, 4, 4],
    [1, 2, 6, 5, 0, 0],
    [6, -6, 4, 4, 10, 3],
    [10, 4, -6, 4, 0, 9],
    [10, 7, 0, -7, 9, 8]])
        price8, p_vector8, q_vector8 = nash_equilibrium.nash_equilibrium(matrix88, 0)
        self.assertEqual(price8, 2.21)  
        np.testing.assert_equal(p_vector8, np.array([0.00,  0.16,  0.42,  0.16, 0.26, 0.00]))
        np.testing.assert_equal(q_vector8, np.array([0.00, 0.38,  0.04, 0.24, 0.34, 0.00]))
        
    def test_n9(self):
        matrix88 = np.array([
    [5, 8, 10],
    [6, 4, 10],
    [0, 0, 0]])
        price9, p_vector9, q_vector9 = nash_equilibrium.nash_equilibrium(matrix88, 0)
        self.assertEqual(price9, 5.60)  
        np.testing.assert_equal(p_vector9, np.array([0.40,  0.60,  0.00]))
        np.testing.assert_equal(q_vector9, np.array([0.80, 0.20,  0.00]))        
        
    def test_n10(self):
        matrix10 = np.array([
    [4, 0, -6, 2, 2, 1],
    [3, 8, 4, -10, 4, 4],
    [1, 2, 6, 5, 0, 0],
    [6, -6, 4, 4, 10, 3],
    [10, 4, -6, 4, 0, 9],
    [10, 7, 0, -7, 9, 8],
    [1, 0, -6, 5, 9, 10],
    [3, -8, 4, -1, 12, 2],
    [1, -2, 3, 5, 9, 0],
    [6, -6, 4, 4, 1, 3],
    [13, 4, -8, 4, 0, 9],
    [1, -7, 0, -7, -5, 8]])
        price10, p_vector10, q_vector10 = nash_equilibrium.nash_equilibrium(matrix10, 0)
        self.assertEqual(price10, 2.76)  
        np.testing.assert_equal(p_vector10, np.array([0.00, 0.00, 0.64, 0.00, 0.05, 0.18]))
        np.testing.assert_equal(q_vector10, np.array([0.00, 0.47, 0.05, 0.30, 0.18, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]))   
        
if __name__ == '__main__':
    unittest.main()
