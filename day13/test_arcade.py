import unittest
from arcade import Arcade, JoyStick
from display import Display
from tile import Tile

class Mock():
    def __init__(self, loc, tile):
        x, y = loc
        self.output = [x,y,tile]
        self.index = -1
    
    def step(self):
        self.index += 1
        if (self.index + 1) % 4:
            return True
        return None

    def set_std_input(self, stdin):
        self.input = stdin

    def get_std_output(self):
        return self.output[self.index%3]

class ArcadeTest(unittest.TestCase):
    def test_joystick_moves(self):
        joystick = JoyStick()
        self.assertEqual(0, joystick.pop())
        joystick.move(-1)
        self.assertEqual(-1, joystick.pop())
        self.assertEqual(0, joystick.pop())
        joystick.move(1)
        self.assertEqual(1, joystick.pop())
        self.assertEqual(0, joystick.pop())
    
    def test_process_paddle(self):
        breakout = Arcade("input.txt", 1)
        breakout.proc = Mock((1,1), Tile.PADDLE)
        breakout.display = Display()
        breakout.tick()
        breakout.tick()
        self.assertEqual(Tile.PADDLE, breakout.field[(1,1)])
        self.assertEqual(False, breakout.running)
    
    def test_process_ball(self):
        breakout = Arcade("input.txt", 1)
        breakout.proc = Mock((1,1), Tile.BALL)
        breakout.display = Display()
        breakout.tick()
        breakout.tick()
        self.assertEqual(Tile.BALL, breakout.field[(1,1)])
        self.assertEqual(False, breakout.running)
    
    def test_process_score(self):
        breakout = Arcade("input.txt", 1)
        breakout.proc = Mock((-1, 0), 12345)
        breakout.display = Display()
        breakout.tick()
        self.assertEqual(12345, breakout.score)
    
    def test_process_automove_left(self):
        breakout = Arcade("input.txt", 1)
        breakout.proc = Mock((3,5), Tile.PADDLE)
        breakout.display = Display()
        breakout.tick()
        breakout.proc = Mock((1,1), Tile.BALL)
        breakout.tick()
        self.assertEqual(1, breakout.ball)
        self.assertEqual(3, breakout.paddle)
        self.assertEqual(-1, breakout.joystick.pop())
    
    def test_process_automove_right(self):
        breakout = Arcade("input.txt", 1)
        breakout.proc = Mock((1,5), Tile.PADDLE)
        breakout.display = Display()
        breakout.tick()
        breakout.proc = Mock((4,1), Tile.BALL)
        breakout.tick()
        self.assertEqual(4, breakout.ball)
        self.assertEqual(1, breakout.paddle)
        self.assertEqual(1, breakout.joystick.pop())
    
    def test_process_automove_stays_still(self):
        breakout = Arcade("input.txt", 1)
        breakout.proc = Mock((2,5), Tile.PADDLE)
        breakout.display = Display()
        breakout.tick()
        breakout.proc = Mock((2,1), Tile.BALL)
        breakout.tick()
        self.assertEqual(2, breakout.ball)
        self.assertEqual(2, breakout.paddle)
        self.assertEqual(0, breakout.joystick.pop())

    def test_process_run(self):
        breakout = Arcade("input.txt", 1)
        breakout.proc = Mock((1,1), Tile.BLOCK)
        breakout.display = Display()
        blocks = breakout.run()
        self.assertEqual(1, blocks)

    def test_answer_matches_actual_solution(self):
        breakout = Arcade("input.txt", 1)
        blocks = breakout.run()
        self.assertEqual(207, blocks)

        breakout = Arcade("input.txt", 2)
        breakout.run()
        self.assertEqual(10247, breakout.score)
