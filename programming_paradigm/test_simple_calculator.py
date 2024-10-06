import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = SimpleCalculator()

    def test_add(self):
        result = self.calculator.add(7, 3)
        self.assertEqual(result, 10)

    def test_subtract(self):
        result = self.calculator.subtract(40, 30)
        self.assertEqual(result, 10)

    def test_multiply(self):
        result = self.calculator.multiply(10, 4)
        self.assertEqual(result, 40)

    def test_divide(self):
        result = self.calculator.divide(10, 2)
        self.assertEqual(result, 5)

    def test_dvivide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(15,0)

if __name__ == '__main__':
    unittest.main()