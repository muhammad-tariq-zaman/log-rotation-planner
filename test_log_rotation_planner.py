import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import days_until_full


class TestRotationPlanner(unittest.TestCase):
    def test_ten_days(self):
        self.assertAlmostEqual(days_until_full(1200, 120), 10.0)

    def test_zero_growth_is_none(self):
        self.assertIsNone(days_until_full(1200, 0))

    def test_fast_growth(self):
        self.assertAlmostEqual(days_until_full(100, 250), 0.4)
