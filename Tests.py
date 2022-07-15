import unittest

from SumOfDigits import sum_of_digits


class MyTestCase(unittest.TestCase):
    def test_sum_of_digits(self):
        result = sum_of_digits(1115)
        self.assertEqual(result, 8)  # add assertion here


if __name__ == '__main__':
    unittest.main()
