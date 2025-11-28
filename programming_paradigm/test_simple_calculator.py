import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-4, -3), -7)
        self.assertEqual(self.calc.add(0, 3), 3)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(4, 3), 1)
        self.assertEqual(self.calc.subtract(5, 7), -2)
        self.assertEqual(self.calc.subtract(-2, 3), -5)
        self.assertEqual(self.calc.subtract(4, -3), 7)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(6, 5), 30)
        self.assertEqual(self.calc.multiply(6, 0), 0)
        self.assertEqual(self.calc.multiply(-4, 5), -20)
        self.assertEqual(self.calc.multiply(-3, -5), 15)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(5, 0), None)
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(4, -2), -2)
