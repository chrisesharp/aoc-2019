import sys
from time import sleep
import subprocess
from opcodes import Processor, get_program
from direction import Direction, next_location, opposite_direction


class Droid:
  WALL        = 0
  CLEAR       = 1
  OXYGEN      = 2
  TILES = {
            0: '#',
            1: '.',
            2: '*'
          }

  def __init__(self, prog):
    self.proc = Processor(prog)
    self.location = (0,0)
    self.top_left = (0,0)
    self.bottom_right = (0,0)
  
  def move(self, move):
    self.location = next_location(self.location, move)
    self.update_extents(self.location)

  def update_extents(self, location):
    self.top_left = (min(self.top_left[0],location[0]), 
                      min(self.top_left[1],location[1]))
    self.bottom_right = (max(self.bottom_right[0], location[0]),
                          max(self.bottom_right[1], location[1]))

  def map_ship(self, computer=None, display=False):
    if not computer:
      computer = self.proc
    oxygen = None
    min_steps = 10**10
    ship_map = {(0, 0): Droid.CLEAR}
    move = Direction.NORTH
    options = {self.location: self.find_options()}
    path = []
    input = []
    computer.set_std_input(input)
    
    while True:  
      backtracking = False    
      if self.location not in options:
        options[self.location] = self.find_options(move)
      if options[self.location]:
        move = options[self.location].pop()
      elif path: 
        backtracking = True
        move = opposite_direction(path.pop())
      else:
        break
      
      tile = computer.run_to_output(move)

      if tile in {self.CLEAR, self.OXYGEN}:
        self.move(move)
        ship_map[self.location] = tile
        
        if not backtracking:
            path.append(move)

        if tile == self.OXYGEN:
          min_steps = min(min_steps, len(path))
          oxygen = self.location
          
        if display: 
          self.display(ship_map)
  
    return oxygen, min_steps, ship_map

  def find_options(self, move=None):
    choices = (Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST)
    non_option = {opposite_direction(move)} if move else {}
    return set(choices).difference(non_option)

  def display(self, ship_map):
    subprocess.call("clear")
    print(render(ship_map, self.bottom_right, self.top_left, self.location))
    sleep(1/30)
  
def render(ship_map, bottom_right, top_left, droid_location):
  width = bottom_right[0] - top_left[0]
  height = bottom_right[1] - top_left[1]
  output_string = ""
  for y in range(height + 1):
    for x in range(width + 1):
      if droid_location == (top_left[0]+ x, top_left[1]+ y):
        output_string += "D"
      else:
        panel = ship_map.get((top_left[0] + x, top_left[1] + y),False)
        output_string += Droid.TILES[panel]
    output_string += "\n"
  return output_string

def neighbours(map, loc):
  (x, y) = loc
  deltas = [(0, -1), (0, 1), (-1, 0), (1, 0)]
  neighbours = [(x + dx, y + dy) for dx, dy in deltas]
  return [n for n in neighbours if n in map and map[n] != Droid.WALL ]


def fill(ship_map, loc, t = 0):
  if ship_map[loc] == Droid.OXYGEN and t != 0:
      return t - 1
  ship_map[loc] = Droid.OXYGEN
  return max([ fill(ship_map, loc, t + 1) for loc in neighbours(ship_map, loc) ])


if __name__ == '__main__':
    file = "input.txt"
    display = False
    if len(sys.argv) > 1:
      display = True
    prog = get_program(file)
    droid = Droid(prog)
    oxygen, min_steps, ship_map = droid.map_ship(droid.proc, display)
    print("Part 1:", min_steps)
    print('Part 2:', fill(ship_map, oxygen))