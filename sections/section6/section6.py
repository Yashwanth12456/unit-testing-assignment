# section6.py — setUpClass + subTest (table-driven tests)

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

class TestCalculationsTableDriven(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # (a, b, sum, diff, prod, quot)
        cls.cases = [
            (8, 2, 10, 6, 16, 4.0),
            (5, 5, 10, 0, 25, 1.0),
            (9, 3, 12, 6, 27, 3.0),
            (-4, 2, -2, -6, -8, -2.0),
        ]

    def test_all_operations_table(self):
        for a, b, s, d, p, q in self.cases:
            with self.subTest(a=a, b=b):
                c = Calculations(a, b)
                self.assertEqual(c.get_sum(), s)
                self.assertEqual(c.get_difference(), d)
                self.assertEqual(c.get_product(), p)
                self.assertEqual(c.get_quotient(), q)

if __name__ == "__main__":
    unittest.main(verbosity=2)
