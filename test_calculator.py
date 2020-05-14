import unittest
from calculator import add
class Calculator_Test(unittest.TestCase):
    """ """
    def test_add(self):
        """Test the add operation of the calculator."""
        self.assertEquals(add(4,6), 10)

unittest.main()