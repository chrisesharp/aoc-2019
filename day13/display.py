import curses
import sys
from time import sleep


class Display:
    def __init__(self, screen=None):
        self.FPS = 0
        self.screen = screen
        if screen:
            self.screen.clear()
            curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
            curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
            curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
            curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
            curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)
            curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
            curses.init_pair(7, curses.COLOR_RED, curses.COLOR_YELLOW)
            self.screen_width = curses.COLS - 1
            self.screen_height = curses.LINES - 1
            self.screen.timeout(1)
            self.pad_origin = (0,0)
    
    def refresh(self, game):
        if self.screen:
            pad = curses.newpad(game.rows + 1, game.columns + 1) if self.screen else None
            if not pad:
                return
            for x, digit in enumerate(str(game.score)):
                pad.addch(0, x, ord(digit))
            for x,y in [(x,y) for y in range(game.rows) for x in range(game.columns)]:
                    tile = game.field.get((x, y),0)
                    pad.addch(y+1, x, ord(str(tile)))
            pad.refresh(self.pad_origin[1],self.pad_origin[0], 0, 0, self.screen_height, self.screen_width)
            self.get_keypress(game)
            sleep(self.FPS)

    def get_keypress(self, game):
        key = self.screen.getch()
        if key >= 0:
            if key == curses.KEY_LEFT:
                game.joystick.move(-1)
            elif key == curses.KEY_RIGHT:
                game.joystick.move(1)
            elif key == curses.KEY_EXIT:
                game.running = False

    def exit(self, game):
        if self.screen:
            width = 20
            height = 5
            y = int(game.rows / 2) - int(height / 2)
            x =  int(game.columns/2) - int(width / 2) 
            msgpad = curses.newpad(height, width)
            msgpad.bkgd(32, curses.color_pair(7))
            msgpad.box()
            msgpad.addstr(2, 5, "GAME OVER")
            msgpad.refresh(0,0, y, x, y + height, x + width)
            self.screen.timeout(-1)
            while self.screen.getch() != 27: continue