import unittest
from opcodes import Processor
from droid import Droid, get_program, fill, render, neighbours
from direction import Direction, opposite_direction, next_location

class Mock():
    def __init__(self, map):
        self.map = map
        self.input = []
        self.location = (0,0)
    
    def set_std_input(self, stdin):
        self.input = stdin

    def run_to_output(self, move):
        next_pos =  next_location(self.location, move)
        if self.map.get(next_pos) == Droid.CLEAR:
            self.location = next_pos
            return 1
        elif self.map.get(next_pos) == Droid.OXYGEN:
            self.location = next_pos
            return 2
        return 0

class DroidTest(unittest.TestCase):    
    def test_opposite_directions(self):
        self.assertEqual(Direction.SOUTH, opposite_direction(Direction.NORTH))
        self.assertEqual(Direction.NORTH, opposite_direction(Direction.SOUTH))
        self.assertEqual(Direction.EAST, opposite_direction(Direction.WEST))
        self.assertEqual(Direction.WEST, opposite_direction(Direction.EAST))

    def test_step_positions(self):
        droid = Droid("")
        droid.move(Direction.WEST)
        self.assertEqual((-1,0),droid.location)
        droid.move(Direction.SOUTH)
        self.assertEqual((-1,1),droid.location)
        droid.move(Direction.EAST)
        self.assertEqual((0,1),droid.location)
        droid.move(Direction.NORTH)
        self.assertEqual((0,0),droid.location)
    
    def test_movement_options_all(self):
        droid = Droid("")
        options = droid.find_options()
        self.assertEqual(options,set([Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST]))
    
    def test_movement_options_for_north_not_south(self):
        droid = Droid("")
        options = droid.find_options(Direction.NORTH)
        self.assertEqual(options,set([Direction.NORTH, Direction.EAST, Direction.WEST]))
    
    def test_display_of_clear_map(self):
        ship_map = {(0, 0): Droid.CLEAR}
        output = render(ship_map, (0,0), (0,0), (0,0))
        self.assertEqual("D\n",output)
    
    def test_display_of_walled_map(self):
        ship_map = {(0, 0): Droid.WALL, (1,0): Droid.WALL,  (2,0): Droid.WALL,
                    (0, 1): Droid.WALL,                     (3,0): Droid.WALL,
                    (0, 2): Droid.WALL, (1,2): Droid.WALL,  (2,2): Droid.WALL}
        output = render(ship_map,(2,2), (0,0), (1,1))
        self.assertEqual("###\n#D#\n###\n",output)
    
    def test_no_neighbours_of_walled_map(self):
        ship_map = {(0, 0): Droid.WALL, (1,0): Droid.WALL,  (2,0): Droid.WALL,
                    (0, 1): Droid.WALL,                     (3,0): Droid.WALL,
                    (0, 2): Droid.WALL, (1,2): Droid.WALL,  (2,2): Droid.WALL}
        output = neighbours(ship_map,(2,2))
        self.assertEqual([],output)
    
    def test_one_neighbour_of_walled_map(self):
        ship_map = {(0, 0): Droid.WALL, (1,0): Droid.WALL,  (2,0): Droid.WALL,
                    (0, 1): Droid.CLEAR,                    (3,0): Droid.WALL,
                    (0, 2): Droid.WALL, (1,2): Droid.WALL,  (2,2): Droid.WALL}
        output = neighbours(ship_map,(1,1))
        self.assertEqual([(0,1)],output)
    
    def test_fill_ship_map(self):
        ship_map = {(0, 0): Droid.WALL, (1,0): Droid.WALL,  (2,0): Droid.WALL,
                    (0, 1): Droid.CLEAR, (1,1): Droid.OXYGEN,(3,0): Droid.CLEAR,
                    (0, 2): Droid.WALL, (1,2): Droid.WALL,  (2,2): Droid.WALL}
        time = fill(ship_map,(1,1))
        self.assertEqual(1, time)
    
    def test_map_of_ship_map(self):
        ship_map = {(-1, -1): Droid.WALL, (0,-1): Droid.WALL,  (1,-1): Droid.WALL, (2,-1): Droid.WALL,
                    (-1, 0): Droid.WALL, (0,0): Droid.CLEAR,(1,0): Droid.OXYGEN, (2,0): Droid.WALL,
                    (-1, 1): Droid.WALL, (0,1): Droid.WALL,  (1,1): Droid.WALL, (2,1): Droid.WALL}
        mock_comp = Mock(ship_map)
        droid = Droid("")
        oxygen, min_steps, output_map = droid.map_ship(mock_comp)
        self.assertEqual({(0, 0): 1, (1, 0): 2}, output_map)
        self.assertEqual(1, min_steps)
        self.assertEqual((1,0), oxygen)

    def test_answer_matches_solution(self):
        file = "input.txt"
        prog = get_program(file)
        droid = Droid(prog)
        oxygen, min_steps, ship_map = droid.map_ship()
        self.assertEqual(246, min_steps)
        self.assertEqual(376, fill(ship_map, oxygen))
