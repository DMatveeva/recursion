import unittest

from EvenIndices import print_elements_with_even_indices
from EvenNumbers import print_even_numbers
from ListsLength import length_of_list
from Palindrome import is_palindrome
from SecondMaxNum import find_second_max_num
from SumOfDigits import sum_of_digits


class MyTestCase(unittest.TestCase):
    def test_sum_of_digits(self):
        result = sum_of_digits(1115)
        self.assertEqual(result, 8)  # add assertion here

    def test_length_of_list(self):
        l = list()
        result = length_of_list(l)
        self.assertEqual(result, 0)  # add assertion here

    def test_is_palindrome(self):
        string = 'a'
        result = is_palindrome(string)
        self.assertEqual(result, True)  # add assertion here

    def test_print_even_numbers(self):
        l = [0, 1, 2, 3, 4, 5, 6, 7]
        result = print_even_numbers(l)

    def test_print_elements_with_even_indices(self):
        l = [0, 1, 2, 3, 4, 5, 6, 7]
        result = print_elements_with_even_indices(l)

    def test_find_second_max_num(self):
        values = [1, 1, 1, -9]
        result = find_second_max_num(values)
        self.assertEqual(result, -9)  # add assertion here


if __name__ == '__main__':
    unittest.main()
