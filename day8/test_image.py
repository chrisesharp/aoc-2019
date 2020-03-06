import unittest
from image import SpaceImage

class TestImage(unittest.TestCase):
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
    
    def test_answer_matches_actual_solution(self):
        file = open("input.txt")
        line = file.readline().rstrip()
        expected = """
1001011100100101111011100
1001010010100101000010010
1001011100100101110010010
1001010010100101000011100
1001010010100101000010000
0110011100011001000010000
"""
        image = SpaceImage(line, 25, 6)
        layer = image.fewest_zeros()
        ones = layer.count(1)
        twos = layer.count(2)
        self.assertEqual(1677, ones * twos)
        self.assertEqual(expected, str(image))

if __name__ == '__main__':
    unittest.main()