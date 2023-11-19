import unittest
import rectangle

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_square_area(self):
        res = rectangle.area(100, 100)
        self.assertEqual(res, 10000)

    def test_negative_side_rectangle_area(self):
        res = area(5, -5)
        self.assertEqual(res, 'The sides of the rectangle cannot be negative')

    def test_zero_perimeter(self):
        res = rectangle.perimeter(0, 5)
        self.assertEqual(res, 0)

    def test_square_perimeter(self):
        res = rectangle.perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_negative_side_rectangle_perimetr(self):
        res = perimeter(5, -5)
        self.assertEqual(res, 'The sides of the rectangle cannot be negative')