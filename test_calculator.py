import Calculators
import unittest
class TestCalculator(unittest.TestCase):
    def test_add(self):
        x = 10
        y = 20
        result = Calculator.add(x,y)
        self.assertEqual(result, x+y)
    def test_sub(self):
        x = 20
        y = 10
        result = Calculator.sub(x,y)
        self.assertEqual(result, x-y)
    def test_mul(self):
        x = 20
        y = 10
        result = Calculator.sub(x,y)
        self.assertEqual(result, x*y)
    def test_div(self):
        x = 20
        y = 10
        result = Calculator.sub(x,y)
        self.assertEqual(result, x/y)