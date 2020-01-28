import unittest
from keys import Grid, is_key, not_wall, shortest_path

class KeysTest(unittest.TestCase):    
    def test_map_parse(self):
        input = """
#########
#b.A.@.a#
#########
"""
        grid = Grid(input.strip().split("\n"))
        self.assertEqual(grid.start_pos[0],(5,1))
        self.assertEqual(grid.allkeys,{'a','b'})

    def test_map_parse_bigger(self):
        input = """
########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################
"""
        grid = Grid(input.strip().split("\n"))
        self.assertEqual(grid.start_pos[0],(15,1))
        self.assertEqual(grid.allkeys,{'a','b','c','d','e','f'})
        self.assertEqual(grid.at((1,1)),'f')
        self.assertTrue(is_key(grid.at((1,1))))
        self.assertTrue(not_wall(grid.at((1,1))))
        self.assertFalse(not_wall(grid.at((0,0))))


    def test_map_find_adjacent_spaces(self):
        input = """
########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################
"""
        grid = Grid(input.strip().split("\n"))
        adjacents = list(grid.get_adjacents((1,1)))
        self.assertEqual(adjacents, [(1,0),(0,1),(1,2),(2,1)])

    def test_map_find_path(self):
        input = """
###########
#b..A@...a#
#####.#####
"""
        grid = Grid(input.strip().split("\n"))
        loc = grid.start_pos[0]
        targets = list(grid.reachable_keys(loc, set()))
        self.assertEqual(targets, [(4, (9, 1), 'a')])
        targets = list(grid.reachable_keys(loc, set('a')))
        self.assertEqual(targets, [(4, (1, 1), 'b')])


    def test_map_choose_ex1(self):
        input = """
########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################
"""
        grid = Grid(input.strip().split("\n"))
        dist = shortest_path(grid)
        self.assertEqual(dist, 86)
    
    def test_map_choose_ex2(self):
        input = """
########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################
"""
        grid = Grid(input.strip().split("\n"))
        dist = shortest_path(grid)
        self.assertEqual(dist, 132)

    def test_map_choose_ex3(self):
        input = """
#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################
"""
        grid = Grid(input.strip().split("\n"))
        dist = shortest_path(grid)
        self.assertEqual(dist, 136)

    def test_map_choose_ex4(self):
        input = """
########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################
"""
        grid = Grid(input.strip().split("\n"))
        dist = shortest_path(grid)
        self.assertEqual(dist, 81)


if __name__ == "__main__":
    unittest.main()