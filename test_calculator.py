import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    # ===================== Test case for addition =====================
    def test_add(self):
        self.assertEqual(self.calc.add(333, 2), 335)

    def test_add(self):
        self.assertEqual(self.calc.add(1658, 320), 1978)

    def test_add(self):
        self.assertEqual(self.calc.add(1, 0), 1)

    def test_add(self):
        self.assertEqual(self.calc.add(0, 0), 0)
    
    # ===================== Test case for substraction =====================
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4052, 569), 3483)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(400, 585), -185)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(555, 555), 0)

    # ===================== Test case for multiplication =====================
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 10), 20)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(485, 25), 12125)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(25, 0), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(0, 3096), 0)

    # ===================== Test case for division =====================
    def test_divide(self):
        self.assertEqual(self.calc.divide(12, 3), 4)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(303, 3), 101)

    def test_divide(self):
        self.assertEqual(self.calc.divide(1028, 7), 146)

    def test_divide(self):
        self.assertEqual(self.calc.divide(11, 8), 1)

    def test_divide(self):
        self.assertEqual(self.calc.divide(1, 1), 1)

    def test_divide(self):
        self.assertEqual(self.calc.divide(128, 128), 1)

    def test_divide(self):
        self.assertEqual(self.calc.divide(0, 6), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 0), "cannot devide by zero")

    # ===================== Test case for modulo =====================
    def test_muldo(self):
        self.assertEqual(self.calc.modulo(25, 7), 4)

    def test_muldo(self):
        self.assertEqual(self.calc.modulo(64, 9), 1)

    def test_muldo(self):
        self.assertEqual(self.calc.modulo(2598, 5), 3)

if __name__ == '__main__':
    unittest.main()