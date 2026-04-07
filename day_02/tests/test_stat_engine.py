import unittest
from src.stat_engine import StatEngine

class TestStatEngine(unittest.TestCase):

    def test_mean(self):
        self.assertEqual(StatEngine([1,2,3,4]).get_mean(), 2.5)

    def test_median_even(self):
        self.assertEqual(StatEngine([1,2,3,4]).get_median(), 2.5)

    def test_median_odd(self):
        self.assertEqual(StatEngine([1,2,3]).get_median(), 2)

    def test_empty(self):
        with self.assertRaises(ValueError):
            StatEngine([])

    def test_std(self):
        data = [2,4,4,4,5,5,7,9]
        self.assertAlmostEqual(
            StatEngine(data).get_standard_deviation(False), 2.0
        )

if __name__ == "__main__":
    unittest.main()