# section5.py — “discovery-style” feel in a single file:
# multiple TestCase classes & multiple tests; run with -v to see names.

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
    def test_all_ops(self):
        c = Calculations(9, 3)
        self.assertEqual(c.get_sum(), 12)
        self.assertEqual(c.get_difference(), 6)
        self.assertEqual(c.get_product(), 27)
        self.assertEqual(c.get_quotient(), 3.0)

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == "__main__":
    unittest.main(verbosity=2)
