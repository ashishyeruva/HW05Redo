import unittest
from triangles import classify_triangle

class TestTriangles(unittest.TestCase):
    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle(5, 5, 5), "Equilateral")

    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(5, 5, 3), "Isosceles")

    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(7,10, 12), "Scalene")

    def test_right_triangle(self):
        self.assertEqual(classify_triangle(6, 8, 10), "Right-angled")

    def test_invalid_triangle(self):
        self.assertEqual(classify_triangle(0, 4, 5), "Not a valid triangle")

    def test_invalid_string_values(self):
         self.assertEqual(classify_triangle("a", "b", "c"), "Not a valid triangle")

    def test_invalid_negetive_values(self):
         self.assertEqual(classify_triangle(-1, 2, 3), "Not a valid triangle")

if __name__ == '__main__':
    unittest.main(exit=False)