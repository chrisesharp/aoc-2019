import unittest
from image import SpaceImage

class TestRun(unittest.TestCase):
    def test_img_3x2(self):
        input = "123456789012"
        image = SpaceImage(input, 3, 2)
        print(image.layers())
        self.assertEqual(2,len(image.layers()))
    
    def test_img_4x3(self):
        input = "123456789012"
        image = SpaceImage(input, 4, 3)
        print(image.layers())
        self.assertEqual(1,len(image.layers()))
    
    def test_img_5x3(self):
        input = "123456789012"
        image = SpaceImage(input, 5, 3)
        print(image.layers())
        self.assertEqual(1,len(image.layers()))
    
    def test_fewest_zeros_img_3x2(self):
        input = "123456789012"
        image = SpaceImage(input, 3, 2)
        layer = image.fewest_zeros()
        print(layer)
        self.assertEqual([1, 2, 3, 4, 5, 6],layer)
    
    def test_img_layering_2x2(self):
        input = "0222112222120000"
        expected = \
"""
01
10
"""
        image = SpaceImage(input, 2, 2)
        picture = str(image)
        print(picture)
        self.assertEqual(expected, picture)

if __name__ == '__main__':
    unittest.main()