import unittest
from math import pi
from circle import area, perimeter

class TestCircle(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0), 0)
    def test_area_positive(self):
        self.assertAlmostEqual(area(5), pi * 25)
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)
    def test_perimeter_positive(self):
        self.assertAlmostEqual(perimeter(5), 2 * pi * 5)

if __name__ == "__main__":
    unittest.main()
