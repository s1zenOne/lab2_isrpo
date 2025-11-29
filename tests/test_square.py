import unittest
from square import area, perimeter

class TestSquare(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0), 0)
    def test_area_positive(self):
        self.assertEqual(area(4), 16)
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)
    def test_perimeter_positive(self):
        self.assertEqual(perimeter(4), 16)

if __name__ == "__main__":
    unittest.main()
