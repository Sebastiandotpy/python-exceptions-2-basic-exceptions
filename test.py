import unittest
from unittest.mock import patch
from solution_calc import MathematicalError, parse_input, calculate





# def calculate(num1, operator, num2):
#     if operator == '+':
#         result = num1 + num2
#     elif operator == '-':
#         result = num1 - num2
#     elif operator == '*':
#         result = num1 * num2
#     elif operator == '/':
#         result = num1 / num2
#     else:
#         raise MathematicalError("Invalid operator: Only +, -, *, and / are supported.")

#     return result


class TestCalculator(unittest.TestCase):

    def test_parse_input_valid(self):
        """Test valid inputs for parse_input function"""
        result = parse_input("1 + 2")
        self.assertEqual(result, (1.0, '+', 2.0))

        result = parse_input("3.5 - 2.1")
        self.assertEqual(result, (3.5, '-', 2.1))

    def test_parse_input_invalid_elements(self):
        """Test invalid inputs with missing elements for parse_input function"""
        with self.assertRaises(MathematicalError):
            parse_input("1 +")

        with self.assertRaises(MathematicalError):
            parse_input("1 + 2 3")

    def test_parse_input_invalid_numbers(self):
        """Test invalid inputs with non-numeric elements for parse_input function"""
        with self.assertRaises(MathematicalError):
            parse_input("a + 2")

        with self.assertRaises(MathematicalError):
            parse_input("1 + b")

    def test_parse_input_invalid_operator(self):
        """Test invalid inputs with unknown operator for parse_input function"""
        with self.assertRaises(MathematicalError):
            parse_input("1 x 2")

        with self.assertRaises(MathematicalError):
            parse_input("3 / 2")

        with self.assertRaises(MathematicalError):
            parse_input("3 ^ 2")  # Additional test case for an invalid operator

    def test_calculate_addition(self):
        """Test addition calculation using calculate function"""
        result = calculate(1.0, '+', 2.0)
        self.assertEqual(result, 3.0)

    def test_calculate_subtraction(self):
        """Test subtraction calculation using calculate function"""
        result = calculate(3.0, '-', 2.0)
        self.assertEqual(result, 1.0)

    def test_calculate_multiplication(self):
        """Test multiplication calculation using calculate function"""
        result = calculate(2.0, '*', 3.0)
        self.assertEqual(result, 6.0)

    # def test_calculate_division(self):
    #     """Test division calculation using calculate function"""
    #     # result = calculate(4.0, '/', 2.0)
    #     self.assertEqual(result, 2.0)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
 