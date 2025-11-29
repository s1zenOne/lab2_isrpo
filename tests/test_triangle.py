import unittest
from triangle import area, perimeter

class TestTriangle(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(5, 0), 0)
    def test_area_positive(self):
        self.assertEqual(area(6, 4), 12)
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0, 0), 0)
    def test_perimeter_positive(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

if __name__ == "__main__":
    unittest.main()
