from unittest import TestCase
import pytest

from main import fibonacci

class FibonacciTests(TestCase):
    def test_returns_correct_fibonacci_number(self):
        correct_sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        for index in range(len(correct_sequence)):
            response = fibonacci(index)
            assert response == correct_sequence[index]

    def test_raise_value_error_on_negative_input(self):
        with pytest.raises(ValueError):
            fibonacci(-1)
