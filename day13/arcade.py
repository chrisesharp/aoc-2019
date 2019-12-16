from opcodes import get_program, Processor
from display import Display
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
    
    def __str__(self):
        return str(self.input)

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
                self.field[(x, y)] = 0
    
    def run(self, screen=None):
        self.screen = Display(screen)
        self.running = True
        self.proc.set_std_input(self.joystick)
        while self.running:
            self.tick()
        self.screen.exit(self)
    
    def tick(self):
        self.screen.display(self)
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
            self.score = tile if tile >= self.score else self.score
        else:
            self.field[(x,y)] = tile
        if tile == 3:
            self.paddle = x
        if tile == 4:
            self.ball = x
        if not self.interactive:
            self.auto_move()
        else:
            self.screen.FPS = 1/50 if self.paddle else 0

    def auto_move(self):
        if self.ball and self.paddle:
            if self.ball < self.paddle:
                self.joystick.move(-1)
            elif self.ball > self.paddle:
                self.joystick.move(1)
            else:
                self.joystick.move(0)


if __name__ == '__main__':
    # print("Part 1:")
    # breakout = Arcade("input.txt", 1)
    # curses.wrapper(breakout.run)
    print("Part 2:")
    breakout = Arcade("input.txt", 2)
    curses.wrapper(breakout.run)
    print("score = ",breakout.score)
    # breakout = Arcade("input.txt", 2, True)
    # curses.wrapper(breakout.run)


