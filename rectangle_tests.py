import unittest
import rectangle

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = rectangle.area(-10, 5)
        self.assertRaises(Value Error, area, -5)

    def test_rectangle_area(self):
        res = rectangle.area(100, 100)
        self.assertEqual(res, 10000)

    def test_rectangle_area(self):
        res = rectangle.area(0, 100)
        self.assertRaises(Value Error, area, 0)

    def test_zero_perimeter(self):
        res = rectangle.perimeter(4, -5)
        self.assertRaises(Value Error, perimetr, -5)

    def test_rectangle_perimeter(self):
        res = rectangle.perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_rectangle_perimetr(self):
        res = perimeter(5, 0)
       self.assertRaises(Value Error, perimetr, 0)
