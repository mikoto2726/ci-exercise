import unittest
from project.calc import fact


class TestTarget(unittest.TestCase):
    def test_fact_positive(self):
        self.assertEqual(fact(1), 1)
        self.assertEqual(fact(5), 120)
