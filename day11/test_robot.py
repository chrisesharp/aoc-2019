import unittest

from robot import Robot
from opcodes import Processor, get_program
from direction import Direction

class RobotTest(unittest.TestCase):    
    def test_step_left_position(self):
        robot = Robot()
        robot.step(0)
        self.assertEqual((-1,0),robot.location)
        self.assertEqual(Direction.LEFT,robot.direction)
        robot.step(0)
        self.assertEqual((-1,1),robot.location)
        self.assertEqual(Direction.DOWN,robot.direction)
        robot.step(0)
        self.assertEqual((0,1),robot.location)
        self.assertEqual(Direction.RIGHT,robot.direction)
        robot.step(0)
        self.assertEqual((0,0),robot.location)
        self.assertEqual(Direction.UP,robot.direction)
    
    def test_step_right_position(self):
        robot = Robot()
        robot.step(1)
        self.assertEqual((1,0),robot.location)
        self.assertEqual(Direction.RIGHT,robot.direction)
        robot.step(1)
        self.assertEqual((1,1),robot.location)
        self.assertEqual(Direction.DOWN,robot.direction)
        robot.step(1)
        self.assertEqual((0,1),robot.location)
        self.assertEqual(Direction.LEFT,robot.direction)
        robot.step(1)
        self.assertEqual((0,0),robot.location)
        self.assertEqual(Direction.UP,robot.direction)
    
    def test_display_panels(self):
        robot = Robot()
        robot.top_left = (0,0)
        robot.bottom_right = (5,5)
        panels = {(0,0):1,(5,0):1,(0,5):1,(5,5):1}
        expected = """
#    #
      
      
      
      
#    #
"""
        self.assertEqual(expected,robot.display_string(panels))
    
    def test_result_matches_actual_solution(self):
        prog = get_program("input.txt")
        processor = Processor(prog, 512, True)
        robot = Robot(processor)
        panels = {(0,0):0}
        panels = robot.run(panels)
        self.assertEqual(2088,len(panels.keys()) )

        processor = Processor(prog, 512, True)
        robot = Robot(processor)
        panels = {(0,0):1}
        panels = robot.run(panels)
        expected = """
 #  # ###   ##   ##  #### #     ##  ###    
 #  # #  # #  # #  # #    #    #  # #  #   
 #  # #  # #    #  # ###  #    #    #  #   
 #  # ###  #    #### #    #    #    ###    
 #  # # #  #  # #  # #    #    #  # #      
  ##  #  #  ##  #  # #    ####  ##  #      
"""
        self.assertEqual(expected, robot.display_string(panels))
