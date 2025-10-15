# section4.py — exception testing with assertRaises

import unittest

class Calculations:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_sum(self):
        return self.a + self.b
    def get_difference(self):
        return self.a - self.b
    def get_product(self):
        return self.a * self.b
    def get_quotient(self):
        # Python will raise ZeroDivisionError when b == 0
        return self.a / self.b

class TestCalculationsExceptions(unittest.TestCase):
    def test_zero_division_raises(self):
        c = Calculations(5, 0)
        with self.assertRaises(ZeroDivisionError, msg="Should raise on division by zero"):
            _ = c.get_quotient()

    def test_normal_division(self):
        c = Calculations(8, 2)
        self.assertEqual(c.get_quotient(), 4)

if __name__ == "__main__":
    unittest.main(verbosity=2)
