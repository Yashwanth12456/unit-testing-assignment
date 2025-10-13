# section1.py — single passing test using unittest.TestCase

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
        return self.a / self.b

class TestCalculations(unittest.TestCase):
    def test_sum(self):
        c = Calculations(8, 2)
        self.assertEqual(c.get_sum(), 10, "The sum is wrong.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
