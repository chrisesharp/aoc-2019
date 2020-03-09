from opcodes import get_program, Processor
from display import Display
from tile import Tile
import curses

class JoyStick():
    def __init__(self):
        self.input = []
    
    def pop(self):
        if len(self.input) > 0:
            return self.input.pop()
        return 0
    
    def move(self, direction):
        self.input = [direction]

class Arcade():
    def __init__(self, file, mem_zero, interactive=False):
        self.interactive = interactive
        prog = get_program(file)
        prog[0] = mem_zero
        self.proc = Processor(prog, 20, True)
        self.columns = 42
        self.rows = 21
        self.field = {}
        self.score = 0
        self.joystick = JoyStick()
        self.ball = None
        self.paddle = None
        for y in range(self.rows):
            for x in range(self.columns):
                self.field[(x, y)] = Tile.EMPTY
    
    def run(self, screen=None):
        self.display = Display(screen)
        self.running = True
        self.proc.set_std_input(self.joystick)
        while self.running:
            self.tick()
        self.display.exit(self)
        return list(self.field.values()).count(Tile.BLOCK)
    
    def tick(self):
        self.display.refresh(self)
        outputs = []
        output = None
        op = None
        while (op := self.proc.step()):
            output = self.proc.get_std_output()
            if output != None:
                outputs.append(output)
            if len(outputs) == 3:
                self.process_outputs(outputs) 
                break
        if op == None:
            self.running = False

    def process_outputs(self, outputs):
        x, y, tile = outputs
        if x == -1:
            self.score = tile
        else:
            tile = Tile(tile)
            self.field[(x,y)] = tile
            if tile == Tile.PADDLE:
                self.paddle = x
            if tile == Tile.BALL:
                self.ball = x
        if not self.interactive:
            self.auto_move()
        else:
            self.display.FPS = 1/30 if self.paddle else 0

    def auto_move(self):
        sign = lambda x: x and (1, -1)[x<0]
        if self.ball and self.paddle:
            self.joystick.move(sign(self.ball - self.paddle))


if __name__ == '__main__':
    breakout = Arcade("input.txt", 1)
    blocks = breakout.run()
    print("Part 1:", blocks)

    breakout = Arcade("input.txt", 2)
    curses.wrapper(breakout.run)
    print("Part 2:", breakout.score)
    
    ## Interactive Mode
    # breakout = Arcade("input.txt", 2, True)
    # curses.wrapper(breakout.run)


