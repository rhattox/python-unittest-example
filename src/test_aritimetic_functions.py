import random
import unittest
from main import add_numbers, divide_numbers, subtract_numbers, multiply_numbers


class TestAddNumbers(unittest.TestCase):

    def test_add_numbers_positive(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_add_numbers_negative(self):
        result = add_numbers(-2, 3)
        self.assertEqual(result, 1)

    def test_add_numbers_zero(self):
        result = add_numbers(0, 0)
        self.assertEqual(result, 0)


class TestMultiplyNumbers(unittest.TestCase):
    def test_multiply_numbers_positive(self):
        result = multiply_numbers(1, 1)
        self.assertEqual(result, 1)

    def test_multiply_numbers_positive_negative(self):
        result = multiply_numbers(1, -1)
        self.assertEqual(result, -1)

    def test_multiply_numbers_negative_negative(self):
        result = multiply_numbers(-1, -1)
        self.assertEqual(result, 1)

    def test_multiply_numbers_by_zero(self):
        result = multiply_numbers(0, random.random())
        self.assertEqual(result, 0)


class TestSubtractNumbers(unittest.TestCase):
    def test_subtract_number(self):
        result = subtract_numbers(1,1)
        self.assertEqual(result,0)

class TestDivideNumbers(unittest.TestCase):
    def test_divide_negative_numbers(self):
        result = divide_numbers(-1,-1)
        self.assertEqual(result,1)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError) as context:
            divide_numbers(random.random(), 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")


if __name__ == '__main__':
    unittest.main()
