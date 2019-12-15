import unittest

from asteroid import get_map, num_visible, best_location, get_angles, find_nth_target

class AsteroidTest(unittest.TestCase):    
    def test_parse_map(self):
        input = """
.#..#
.....
#####
....#
...##
"""
        expected = {(1,0),(4,0),(0,2),(1,2),(2,2),(3,2),(4,2),(4,3),(3,4),(4,4)}
        output = get_map(input)
        self.assertEqual(expected,output)
    
    def test_A_and_B_see_7_map(self):
        input = """
.A..B
.....
#####
....C
...D#
"""
        map = get_map(input)
        A = (1,0)
        B = (4,0)
        C = (4,3)
        D = (3,4)
        self.assertEqual(7,num_visible(A, map))
        self.assertEqual(7,num_visible(B, map))
        self.assertEqual(7,num_visible(C, map))
        self.assertEqual(8,num_visible(D, map))
        self.assertEqual(D,best_location(map)[0])
        self.assertEqual(8,best_location(map)[1])
    
    def test_ex1_map(self):
        input = """
......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
"""
        map = get_map(input)
        best = best_location(map)
        self.assertEqual((5,8), best[0])
        self.assertEqual(33,best[1])
    
    def test_ex2_map(self):
        input = """
.#....###24...#..
##...##.13#67..9#
##...#...5.8####.
..#.....X...###..
..#.#.....#....##
"""
        map = get_map(input)
        target_1 = (8,1)
        target_9 = (15,1)
        laser = (8,3)
        asteroid = find_nth_target(1, laser, map)
        self.assertEqual(target_1, asteroid)
        asteroid = find_nth_target(9, laser, map)
        self.assertEqual(target_9, asteroid)
    

if __name__ == '__main__':
    unittest.main()