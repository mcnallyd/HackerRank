#https://www.hackerrank.com/challenges/ctci-array-left-rotation

def array_left_rotation(a, n, k):
    """
    n = number of in tegers in a
    k = number of left rotation to perform
    a = array of integers
    """
    if (not a) or (k == 0) or (k%n == 0):
        return a
    k = k%n
    a = a[k:] + a[:k]
    return a

import unittest

class TestSolution(unittest.TestCase):
    
    def test_array_left_rotation_empty_array(self):
        expected = []
        actual = array_left_rotation([], 0, 20)
        self.assertEqual(expected, actual)

    def test_array_left_rotation_k_less_than_n(self):
        expected = [3,4,1,2]
        actual = array_left_rotation([1,2,3,4], 4, 2)
        self.assertEqual(expected, actual)

    def test_array_left_rotation_k_greater_than_n(self):
        expected = [1,2,3,4]
        actual = array_left_rotation([1,2,3,4], 4, 12)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
