from unittest import TestCase

from main import fibonacci

class FibonacciTests(TestCase):
    def test_returns_correct_fibonacci_number(self):
        correct_sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        for index in range(len(correct_sequence)):
            response = fibonacci(index)
            self.assertEqual(response, correct_sequence[index])

    def test_raise_value_error_on_negative_input(self):
        self.assertRaises(ValueError, fibonacci, -1)
