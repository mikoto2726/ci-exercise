import unittest
from project.calc import fact, gcb


class TestTarget(unittest.TestCase):
    def test_fact_positive(self):
        self.assertEqual(fact(1), 1)
        self.assertEqual(fact(5), 120)

    def test_fact_zero(self):
        self.assertEqual(fact(0), 1)
    
    def test_fact_negative(self):
        with self.assertRaises(ValueError):
            fact(-1)

    def test_gcb(self):
        self.assertEqual(gcb(12, 8), 4)
        self.assertEqual(gcb(14, 28), 14)
        self.assertEqual(gcb(21, 14), 7)
        self.assertEqual(gcb(56, 48), 8)
        self.assertEqual(gcb(77, 42), 7)

