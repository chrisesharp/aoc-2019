import unittest


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


if __name__ == '__main__':
    unittest.main()