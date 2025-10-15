# section2.py — four operations tested with assertEqual

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

class TestCalculationsAll(unittest.TestCase):
    def test_sum(self):
        c = Calculations(8, 2)
        self.assertEqual(c.get_sum(), 10, "The sum is wrong.")
    def test_difference(self):
        c = Calculations(8, 2)
        self.assertEqual(c.get_difference(), 6, "The difference is wrong.")
    def test_product(self):
        c = Calculations(8, 2)
        self.assertEqual(c.get_product(), 16, "The product is wrong.")
    def test_quotient(self):
        c = Calculations(8, 2)
        self.assertEqual(c.get_quotient(), 4, "The quotient is wrong.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
