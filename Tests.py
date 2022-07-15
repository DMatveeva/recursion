import unittest

from ListsLength import length_of_list
from SumOfDigits import sum_of_digits


class MyTestCase(unittest.TestCase):
    def test_sum_of_digits(self):
        result = sum_of_digits(1115)
        self.assertEqual(result, 8)  # add assertion here

    def test_length_of_list(self):
        l = list()
        result = length_of_list(l)
        self.assertEqual(result, 0)  # add assertion here


if __name__ == '__main__':
    unittest.main()
