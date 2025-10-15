# section3.py — refactor using setUp to remove duplication

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

class TestCalculationsWithSetUp(unittest.TestCase):
    def setUp(self):
        self.c = Calculations(8, 2)

    def test_sum(self):
        self.assertEqual(self.c.get_sum(), 10)
    def test_difference(self):
        self.assertEqual(self.c.get_difference(), 6)
    def test_product(self):
        self.assertEqual(self.c.get_product(), 16)
    def test_quotient(self):
        self.assertEqual(self.c.get_quotient(), 4)

if __name__ == "__main__":
    unittest.main(verbosity=2)
