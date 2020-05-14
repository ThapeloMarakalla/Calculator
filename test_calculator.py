import unittest
from calculator import add, subtract
class Calculator_Test(unittest.TestCase):
    """ """
    def test_add(self):
        """Test the add operation of the calculator."""
        self.assertEquals(add(4,6), 10)

    def test_subtract(self):
        """Test the subtract operation of the calculator."""
        self.assertEquals(subtract(10,5), 5)

unittest.main()