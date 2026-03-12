from unittest import TestCase
from app import divide, multiply


class TestFunctions(TestCase):
    def test_divide_result(self):
        divident = 10
        divisor = 2
        expected_result = 5.0
        result = divide(divident, divisor)
        self.assertAlmostEqual(result, expected_result, delta=0.0001)

    def test_negative_result(self):
        divident = -10
        divisor = 2
        expected_result = -5.0
        result = divide(divident, divisor)
        self.assertAlmostEqual(result, expected_result, delta=0.0001)

    def test_divide_by_zero(self):
        divident = 10
        divisor = 0
        with self.assertRaises(ZeroDivisionError):
            divide(divident, divisor)

    def test_invalid_types(self):
        divident = "10"
        divisor = "2"
        with self.assertRaises(TypeError):
            divide(divident, divisor)

        divident = 10
        divisor = "2"
        with self.assertRaises(TypeError):
            divide(divident, divisor)

        divident = "10"
        divisor = 2
        with self.assertRaises(TypeError):
            divide(divident, divisor)

    def test_divident_zero(self):
        divident = 0
        divisor = 2
        expected_result = 0
        result = divide(divident, divisor)
        self.assertAlmostEqual(result, expected_result)

    def test_divident_error_on_zero(self):
        self.assertRaises(ValueError, lambda: divide(25, 0))
        # with self.assertRaises(ValueError):
        #     divide(25, 0)

    def test_multiply_empty(self):
        # self.assertRaises(ValueError, lambda: multiply())
        with self.assertRaises(ValueError):
            multiply()

    def test_multiply_single_value(self):
        expected = 15
        self.assertEqual(multiply(expected), expected)

    def test_multiply_by_zero(self):
        expected = 0
        self.assertEqual(multiply(expected), expected)

    def test_multiply_result(self):
        inputs = (10, 2, 4, 8)
        result = multiply(*inputs)
        expected_result = 640
        self.assertEqual(result, expected_result)

    def test_multiply_result_with_zero(self):
        inputs = (10, 2, 0, 8)
        result = multiply(*inputs)
        expected_result = 0
        self.assertEqual(result, expected_result)

    def test_multiply_result_with_negative(self):
        inputs = (10, 2, -1, 8)
        result = multiply(*inputs)
        expected_result = -160
        self.assertEqual(result, expected_result)

    def test_multiply_result_with_float(self):
        inputs = (10, 2.5, 5)
        result = multiply(*inputs)
        expected_result = 125.0
        self.assertEqual(result, expected_result)
