import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(1, 0), 1)
        self.assertEqual(self.calc.add(10000, 15000), 25000)
        self.assertEqual(self.calc.add(-10.5, -1.2), -11.7)
        self.assertEqual(self.calc.add(5.0, -2.5), 2.5)
        self.assertEqual(self.calc.add(3.7, 4.2), 7.9)

    def test_subtraction(self):
        """Test the addition method."""
        self.assertEqual(self.calc.subtract(4, 8), -4)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-10, 5), -15)
        self.assertEqual(self.calc.subtract(-5, -4), -1)
        self.assertEqual(self.calc.subtract(17, 0), 17)
        self.assertEqual(self.calc.subtract(21000, 7000), 14000)
        self.assertEqual(self.calc.subtract(-9.0, -3.2), -5.8)
        self.assertEqual(self.calc.subtract(7.0, -5.0), 12)
        self.assertAlmostEqual(self.calc.subtract(9.2, 4.8), 4.4)

    def test_multiplication(self):
        """Test the addition method."""
        self.assertEqual(self.calc.multiply(5, 7), 35)
        self.assertEqual(self.calc.multiply(-5, 8), -40)
        self.assertEqual(self.calc.multiply(-8, -7), 56)
        self.assertEqual(self.calc.multiply(21, 0), 0)
        self.assertEqual(self.calc.multiply(10, 0), 0)
        self.assertEqual(self.calc.multiply(10000, 5000), 50000000)
        self.assertEqual(self.calc.multiply(-4.5, -9.7), 43.65)
        self.assertEqual(self.calc.multiply(5.0, -9.2), -46.0)
        self.assertAlmostEqual(self.calc.multiply(11.2, 3.8), 42.56)

    def test_division(self):
        """Test the addition method."""
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(-8, 4), -2)
        self.assertEqual(self.calc.divide(-20, -3), 6.666666666666667)
        self.assertEqual(self.calc.divide(45000, 7000), 6.428571428571429)
        self.assertEqual(self.calc.divide(-7.8, -9.7), 0.8041237113402062)
        self.assertEqual(self.calc.divide(4.5, -5.6), -0.8035714285714286)
        self.assertAlmostEqual(self.calc.divide(9.2, 8.4), 1.095238095)
        self.assertEqual(self.calc.divide(0, 10), 0)
        self.assertEqual(self.calc.divide(0, -5), 0)
        self.assertEqual(self.calc.divide(0, 5.0), 0)
        self.assertEqual(self.calc.divide(0, -8.4), 0)

    def test_divide_by_zero(self):
        """Test the addition method."""
        self.assertRaises(ZeroDivisionError, self.calc.divide, 10, 0)
        self.assertRaises(ZeroDivisionError, self.calc.divide, -20, 0)
        self.assertRaises(ZeroDivisionError, self.calc.divide, 9.2, 0)
        self.assertRaises(ZeroDivisionError, self.calc.divide, -4.8, 0)
        self.assertRaises(ZeroDivisionError, self.calc.divide, 0, 0)


if __name__ == '__main__':
    unittest.main()


