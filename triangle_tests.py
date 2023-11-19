import unittest
import triangle

class TestTriangleCase(unittest.TestCase):
    def test_positive_area(self):
        res = triangle.area(10, 6)
        self.assertEqual(res, 30)

    def test_zero_area(self):
        res = triangle.area(0, 5)
        self.assertEqual(res, 0)

    def test_negative_side_triangle_area(self):
        res = area(4, -5)
        self.assertEqual(res, 'The base and height cannot be negative')

    def test_positive_perimeter(self):
        res = triangle.perimeter(10, 5, 8)
        self.assertEqual(res, 23)

    def test_zero_perimetr(self):
        res = triangle.perimeter(5, 3, 0)
        self.assertEqual(res, 0)

    def test_negative_side_triangle_perimetr(self):
        res = perimeter(4, 5, -6)
        self.assertEqual(res, 'The base and height cannot be negative')
