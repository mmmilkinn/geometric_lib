import unittest
import rectangle

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = rectangle.area(10, 0)
        self.assertRaises(Value Error, area, 0)

    def test_rectahgle_area(self):
        res = rectangle.area(100, 100)
        self.assertEqual(res, 10000)

    def test_rectahgle_area(self):
        res = rectangle.area(0, 100)
        self.assertEqual(res, 10000)

    def test_zero_perimeter(self):
        res = rectangle.perimeter(0, 5)
        self.assertRaises(Value Error, perimetr, 0)

    def test_rectangle_perimeter(self):
        res = rectangle.perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_rectangle_perimetr(self):
        res = perimeter(5, 5)
        self.assertEqual(res, 20)
