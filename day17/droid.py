import sys
from time import sleep
from functools import reduce
from opcodes import Processor, get_program
from direction import Direction, next_location, left, right


class Droid:
  tiles = {
    ord("^") : Direction.UP,
    ord("<") : Direction.LEFT,
    ord(">") : Direction.RIGHT,
    ord("v") : Direction.DOWN
  }
  
  SCAFFOLD = 35
  NEWLINE = 10
  
  FUNCS = [ "A", "B", "C"]

  def __init__(self, prog):
    self.prog = prog
    self.proc = Processor(prog, 10000)
    self.top_left = (0,0)
    self.bottom_right = (0,0)
    self.width = 0
    self.height = 0
    self.scaffold = []

  def clean(self, input):
    self.prog[0] = 2
    self.proc = Processor(self.prog, 10000)
    flat_input = [item for sublist in input for item in reversed(list(map(ord,sublist))) ]
    self.reset_extents()
    layout , _ = self.camera_view(flat_input)
    return layout

  def reset_extents(self):
    self.top_left = (0,0)
    self.bottom_right = (0,0)
    self.width = 0
    self.height = 0

  def update_extents(self, location):
    self.top_left = (min(self.top_left[0],location[0]),  min(self.top_left[1],location[1]))
    self.bottom_right = (max(self.bottom_right[0], location[0]), max(self.bottom_right[1], location[1]))
    self.width = self.bottom_right[0] - self.top_left[0]
    self.height = self.bottom_right[1] - self.top_left[1]

  def camera_view(self, input=[]):
    self.proc.set_std_input(input)
    layout = {}
    x,y = (0,0)
    droid = (0,0)
    tile = None
    while tile := self.proc.run_to_output():
      if tile == Droid.NEWLINE:
        x = 0
        y += 1
        continue
      if tile in Droid.tiles:
        droid = (x,y)
        self.direct = Droid.tiles[tile]
        self.scaffold.append((x,y))
      if tile == Droid.SCAFFOLD:
        self.scaffold.append((x,y))
      layout[(x,y)] = tile
      self.update_extents((x,y))
      x += 1
    return layout, droid

  def find_intersections(self):
    width = self.bottom_right[0] - self.top_left[0]
    height = self.bottom_right[1] - self.top_left[1]
    return [(x,y) for y in range(height + 1) for x in range(width + 1) if len(scaffolds(self.scaffold, (x,y))) == 5 ]

  def display(self, view):
    output_string = ""
    for y in range(self.height + 1):
      for x in range(self.width + 1):
        output_string += chr(view.get((x, y),32))
      output_string += "\n"
    return output_string

  
  def find_path(self, map, location):
    path = []
    steps = 0
    while True:
      next_step = next_location(location, self.direct)
      if next_step in self.scaffold:
        steps += 1
        location = next_step
        continue
      else:
        if steps:
          path.append(str(steps))
          steps = 0
        if next_location(location, left(self.direct)) in self.scaffold:
          self.direct = left(self.direct)
          path.append("L")
        elif next_location(location, right(self.direct)) in self.scaffold:
          self.direct = right(self.direct)
          path.append("R")
        else:
          break
    return path

def scaffolds(map, loc):
  (x, y) = loc
  deltas = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
  neighbours = [(x + dx, y + dy) for dx, dy in deltas]
  return [n for n in neighbours if n in map]

def find_factors(path):
  path_repr = ",".join(path)
  index = 0
  length = len(path)
  hits = {}
  while index < len(path)-1:
    func = ",".join(path[index:index+length])
    if len(func) > 20 or any(letter in func for letter in Droid.FUNCS):
      length -= 1
      continue
    if length == 0:
      index += 1
      length = len(path)
      continue
    occurences = path_repr.count(func)
    if occurences:
      hits[func]=occurences
      length -= 1
    else:
      break
  return [func for func, _ in sorted(hits.items(), key=lambda item: item[1]* len(item[0]))]

def refactor(index, func, path):
  func_name = Droid.FUNCS[index]
  return ",".join(path).replace(func+",",func_name+",").replace(","+func,","+func_name).replace(func,func_name).split(",")

def factorize(path):
  options = find_factors(path)
  factor = options.pop()
  path_opts = {}
  path_opts[str(path)]=options
  queue = [factor]
  chosen = []
  paths = [path]
  func = None
  func_index = 0
  while func := queue.pop():
    new_path = refactor(func_index, func, path)
    if len(new_path) < len(path):
      paths.append(new_path)
      func_index += 1
      chosen.append(func)
      if not path_opts.get(str(new_path)):
        path_opts[str(new_path)] = find_factors(new_path)
    path = paths[-1]
    
    if is_complete(path):
      break
    
    while (len(chosen) == 3) or (not path_opts[str(path)]):
      chosen.pop()
      paths.pop()
      path = paths[-1]
      func_index -= 1

    queue.append(path_opts[str(path)].pop())
  return chosen, ",".join(path)
    

def is_complete(path):
  return len([x for x in path if x not in Droid.FUNCS]) == 0


if __name__ == '__main__':
    file = "input.txt"
    prog = get_program(file)
    droid = Droid(prog)
    view, start = droid.camera_view()
    intersections = droid.find_intersections()
    print(droid.display(view))
    print("Part 1:")
    print(reduce((lambda x,y: x+y), list(map(lambda x: x[0] * x[1], intersections))))

    print('Part 2:')
    print("Factoring functions from path")
    funcs, path = factorize(droid.find_path(view, start))
    input =["n\n"]
    for i in list(reversed(funcs)):
      input.append(i + "\n")
    input.append(path + "\n")
    print("Running droid with program")
    output = droid.clean(input)
    answer_loc = (0,droid.bottom_right[1])
    # print(droid.display(output))
    print("Answer: ", output[answer_loc])