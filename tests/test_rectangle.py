import unittest
from rectangle import area, perimeter

class TestRectangle(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(5, 0), 0)
    def test_area_positive(self):
        self.assertEqual(area(5, 3), 15)
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0), 0)
    def test_perimeter_positive(self):
        self.assertEqual(perimeter(5, 3), 16)

if __name__ == "__main__":
    unittest.main()
