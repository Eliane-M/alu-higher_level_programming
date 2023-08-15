"""unittest for the function def max_integer(list=[]):"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestStringMethods(unittest.TestCase):
    """
    the unittest for def max_integer(list=[]):
    """
    def test_empty_list(self):
        string = []
        self.assertEqual(max_integer(string), None)
    def test_list_with_one_element(self):
        List = [1]
        self.assertEqual(max_integer(List), 1)
    def test_arranged_list(self):
        List = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(max_integer(List), 7)
    def test_disorganised_list(self):
        List = [3, 5, 2 , 1, 7, 6 ,4]
        self.assertEqual(max_integer(List), 7)
    def test_one_negative_number(self):
        List = [1, 3, 2, 4, -5, 7, 6]
        self.assertEqual(max_integer(List), 7)
    def test_only_negative_numbers(self):
        List = [-1, -2, -3, -4 ,-5 , -6]
        self.assertEqual(max_integer(List), -1)
    def test_max_in_the_middle(self):
        List = [2, 3, 1, 4, 7, 6, 5]
        self.assertEqual(max_integer(List), 7)
    def test_max_at_beginning(self):
        List = [7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(max_integer(List), 7)
    def test_only_floats(self):
        List = [3.14, 2.45, 2.85, 4.29, 6.49]
        self.assertEqual(max_integer(List), 6.49)
    def test_with_one_float(self):
        List = [1, 3, 2, 4.58, 8]
        self.assertEqual(max_integer(List), 8)
    def test_with_a_string(self):
        List = [1, 2, 3, 4, 'red']
