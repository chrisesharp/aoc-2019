import unittest
from opcodes import Processor
from droid import Droid
from direction import Direction

class DroidTest(unittest.TestCase):    
    def test_step_left_position(self):
        droid = Droid()
        droid.step(Direction.WEST)
        self.assertEqual((-1,0),droid.location)
        droid.step(Direction.SOUTH)
        self.assertEqual((-1,1),droid.location)
        droid.step(Direction.EAST)
        self.assertEqual((0,1),droid.location)
        droid.step(Direction.NORTH)
        self.assertEqual((0,0),droid.location)