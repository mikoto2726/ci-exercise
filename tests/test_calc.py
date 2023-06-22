import unittest
from project.calc import fact


class TestTarget(unittest.TestCase):
    def test_fact_positive(self):
        self.assertEqual(fact(1), 1)
        self.assertEqual(fact(5), 120)

    def test_fact_zero(self):
        self.assertEqual(fact(0), 1)
    
    def test_fact_negative(self):
        with self.assertRaises(ValueError):
            fact(-1)
