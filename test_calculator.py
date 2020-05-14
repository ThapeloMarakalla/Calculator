import unittest
from calculator import add, subtract, multiply, divide
class Calculator_Test(unittest.TestCase):
    """ """
    def test_add(self):
        """Test the add operation of the calculator."""
        self.assertEqual(add(4,6), 10)

    def test_subtract(self):
        """Test the subtract operation of the calculator."""
        self.assertEqual(subtract(10,5), 5)

    def test_multiply(self):
        """Test the multiply operation of the calculator."""
        self.assertEqual(multiply(2,6), 12)

    def test_divid(self):
        """Test the divide operation of the calculator."""
        self.assertEqual(divide(9,3), 3)

unittest.main()